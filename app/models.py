from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)

    def __repr__(cls):
        return '<Author {}>'.format(cls.name)


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    synopsis = db.Column(db.Text, nullable=True)
    cover = db.Column(db.String(256), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    author = db.relationship('Author', backref='books')

    def __repr__(cls):
        return '<Book {}>'.format(cls.name)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(64), unique=True, nullable=False
    )
    password = db.Column(db.String(256), nullable=False)

    def __repr__(cls):
        return '<User {}>'.format(cls.username)


class UsersBook(db.Model):
    __tablename__ = 'users_books'

    book_id = db.Column(
        db.Integer, db.ForeignKey('books.id'), primary_key=True
    )
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), primary_key=True
    )
    rating = db.Column(db.Float, nullable=True)
    status = db.Column(db.String(256))

    book = db.relationship('Book', backref='users_book')
    user = db.relationship('User', backref='users_book')

    @classmethod
    def average_rating(cls):
        """
        Takes average rating of every book by book_id and creates dictionary
        so ratings can be matched with proper book in view.
        """

        avg_rating = db.session.query(cls.book_id, func.avg(
            cls.rating)).group_by(cls.book_id).all()

        return dict(avg_rating)

    def __repr__(cls):
        return '<Reading {}{}>'.format(cls.book_id, cls.user_id)
