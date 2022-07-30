# -*- coding: utf-8 -*-
from flask import render_template, send_from_directory

from reader import app
from reader.models import Book


@app.route("/")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)


@app.route("/uploads/<filename>")
def send_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/<int:book_id>")
def book(book_id):
    book_ = Book.query.get_or_404(book_id)
    return render_template("book.html", book=book_)
