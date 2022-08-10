# -*- coding: utf-8 -*-
from flask import Flask
from flask_migrate import Migrate

from reader.models import db
from reader.routes import blueprint as book_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object("reader.config.DevelopmentConfig")
    app.app_context().push()
    db.init_app(app)
    Migrate(app, db)
    app.register_blueprint(book_blueprint)
    return app
