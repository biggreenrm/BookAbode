# -*- coding: utf-8 -*-
from flask import Flask

from reader.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object("reader.config.Config")
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    db.session.commit()
    from reader.routes import blueprint

    app.register_blueprint(blueprint)
    return app
