# -*- coding: utf-8 -*-
from flask import Flask

from reader.fixtures import add_default_books
from reader.models import Book, db
from reader.routes import blueprint as book_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object("reader.config.Config")
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    db.session.commit()
    books = Book.query.all()
    if not books:
        add_default_books()
    app.register_blueprint(book_blueprint)
    return app
