# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("reader.config.Config")
    db.init_app(app)
    from reader.routes import blueprint

    app.register_blueprint(blueprint)
    return app
