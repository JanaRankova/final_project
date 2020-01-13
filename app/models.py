from . import db
from flask_login import UserMixin


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)

    def __repr__(self):
        return '<Author {}>'.format(self.name)


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    synopsis = db.Column(db.Text, nullable=True)
    cover = db.Column(db.String(256), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    author = db.relationship('Author', backref='books')

    def __repr__(self):
        return '<Book {}>'.format(self.name)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(64), unique=True, nullable=False
    )
    password = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)


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

    def __repr__(self):
        return '<Reading {}{}>'.format(self.book_id, self.user_id)
