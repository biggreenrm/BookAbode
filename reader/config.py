# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = os.getenv("DEBUG", False)
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        "sqlite:///" + os.path.join(basedir, "database.db"),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)
    SECRET_KEY = os.getenv("SECRET_KEY", "hard to guess string")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
