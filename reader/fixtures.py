# -*- coding: utf-8 -*-
import json
import os

from reader.models import Book

books_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "books.json"))


def add_default_books():
    from reader import db
    with open(books_file) as f:
        books = json.load(f)
        for book in books:
            db.session.add(Book(**book))
    db.session.commit()


if __name__ == "__main__":
    add_default_books()
