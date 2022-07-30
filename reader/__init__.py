# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

# Config
UPLOAD_FOLDER = "uploads"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True  # possibly disable
app.config["SECRET_KEY"] = "hard to guess string"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Database
db = SQLAlchemy(app)

from reader import models, routes
