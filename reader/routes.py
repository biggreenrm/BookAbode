# -*- coding: utf-8 -*-
from flask import render_template, request, send_from_directory

from reader import app
from reader.models import Book


@app.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    books = Book.query.order_by(Book.created_at.desc()).paginate(page=page, per_page=4)
    return render_template("index.html", books=books)


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


@app.route("/uploads/<filename>")
def send_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/<int:book_id>")
def book(book_id):
    book_ = Book.query.get_or_404(book_id)
    return render_template("book.html", book=book_)
