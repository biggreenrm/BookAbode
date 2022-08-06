# -*- coding: utf-8 -*-
import os
import secrets

from flask import (
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from PIL import Image
from sqlalchemy.exc import IntegrityError

from reader import app, db
from reader.forms import BookForm, UpdateBookForm
from reader.models import Book


# TODO: move to helpers.py
def save_picture(cover):
    """Save picture to upload folder folder and
    give it a random name."""

    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(cover.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, app.config["UPLOAD_FOLDER"], picture_fn)
    output_size = (220, 240)
    image = Image.open(cover)
    image.thumbnail(output_size)
    image.save(picture_path)
    return picture_fn


@app.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    books = Book.query.order_by(Book.created_at.desc()).paginate(page=page, per_page=4)
    return render_template("index.html", books=books)


@app.route("/uploads/<filename>")
def send_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/create/", methods=("GET", "POST"))
def create():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(
            title=form.title.data,
            author=form.author.data,
            genre=form.genre.data,
            rating=int(form.rating.data),
            description=form.description.data,
            notes=form.notes.data,
            cover=(save_picture(form.cover.data) if form.cover.data else "default.jpg"),
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("create.html", form=form)


@app.route("/<int:book_id>/edit/", methods=("GET", "POST"))
def edit(book_id):
    book = Book.query.get_or_404(book_id)
    form = UpdateBookForm()
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.genre = form.genre.data
        book.rating = int(form.rating.data)
        book.description = form.description.data
        book.notes = form.notes.data
        book.cover = save_picture(form.cover.data) if form.cover.data else book.cover
        try:
            db.session.commit()
            return redirect(url_for("index"))
        except IntegrityError:
            db.sessiom.rollback()
            flash("Mistake: such book already exists")
            return render_template("edit.html", form=form)

    elif request.method == "GET":
        form.title.data = book.title
        form.author.data = book.author
        form.genre.data = book.genre
        form.rating.data = book.rating
        form.cover.data = book.cover
        form.description.data = book.description
        form.notes.data = book.notes

    return render_template("edit.html", form=form)


@app.post("/<int:book_id>/delete/")
def delete(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/thrillers/")
def thrillers():
    page = request.args.get("page", 1, type=int)
    books = Book.query.filter(Book.genre == "триллер").paginate(page=page, per_page=4)
    return render_template("thrillers.html", books=books)


@app.route("/best/")
def best():
    page = request.args.get("page", 1, type=int)
    books = Book.query.filter(Book.rating > 4).paginate(page=page, per_page=4)
    return render_template("thrillers.html", books=books)


@app.route("/<int:book_id>")
def book(book_id):
    book_ = Book.query.get_or_404(book_id)
    return render_template("book.html", book=book_)
