# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

from reader.models import Book


class BookForm(FlaskForm):
    title = StringField("Название", validators=[DataRequired(), Length(min=5, max=100)])
    author = StringField("Автор", validators=[DataRequired(), Length(min=5, max=100)])
    genre = StringField("Жанр", validators=[DataRequired(), Length(min=5, max=20)])
    cover = FileField("Обложка книги", validators=[FileAllowed(["jpg", "png"])])
    rating = IntegerField("Моя оценка", validators=[NumberRange(min=1, max=5)])
    description = TextAreaField("Сюжет", validators=[DataRequired(), Length(max=500)])
    notes = TextAreaField("Заметки", validators=[DataRequired(), Length(max=500)])
    submit = SubmitField("Добавить")

    def validate_title(self, title):
        book = Book.query.filter_by(title=title.data).first()
        if book:
            raise ValidationError("Такая книга уже есть в списке прочитанных")


class UpdateBookForm(FlaskForm):
    title = StringField("Название", validators=[DataRequired(), Length(min=5, max=100)])
    author = StringField("Автор", validators=[DataRequired(), Length(min=5, max=100)])
    genre = StringField("Жанр", validators=[DataRequired(), Length(min=5, max=20)])
    cover = FileField("Обложка книги", validators=[FileAllowed(["jpg", "png"])])
    rating = IntegerField("Моя оценка", validators=[NumberRange(min=1, max=5)])
    description = TextAreaField("Сюжет", validators=[DataRequired(), Length(max=500)])
    notes = TextAreaField("Заметки", validators=[DataRequired(), Length(max=500)])
    submit = SubmitField("Обновить")
