# -*- coding: utf-8 -*-
import json
import os

from reader import db
from reader.models import Book

books_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "books.json"))

if __name__ == "__main__":
    with open(books_file) as f:
        books = json.load(f)
        for book_ in books:
            book = Book(**book_)
            db.session.add(book)
        db.session.commit()
