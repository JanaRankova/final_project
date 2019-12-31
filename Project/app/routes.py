from flask import  url_for, request, render_template, make_response, flash, redirect
from flask import current_app as app
from flask_login import login_required, logout_user, current_user, login_user
from . import loginManager
from . import db
#from .forms import RegistrationForm, LoginForm
from .models import Book, Author, UsersBook, User

@app.route('/')
def index():
    return 'Hello There'

@app.route('/list/')
def list_of_books():
    """Creates a list of all books in database. User can browse list and choose a book from it."""

    return render_template('/list_of_all_books.html',
    all_books = Book.query.all())

# @app.route('/profile/<username>')
# def filter_users():


#     return render_template()

@loginManager.user_loader
def load_user(user_id):
    """Loads user as a current_user."""

    if user_id:
        return User.query.get(user_id)

    return None

@app.errorhandler(404)
def not_found(_):
    """Creates own custom view for 404 error."""

    return make_response(
        render_template('/404.html'),
        404
    )

@app.context_processor
def inject_user():
    """Inject data of current user into templates and forms."""

    return dict(
        user = current_user
    )

@app.route('/db')
def populatedb():
    """Populates db with fake data."""


    # if False:
    ####first create authors####

        # john_smith = Author(name = 'John Smith')
        # db.session.add(john_smith)
        # db.session.commit()

    ####create books and users#### cant i just simply use session.flush() between to make two separete sessions?
    ####P.S.: append() is not working properly####

        # a = db.session.query(Author).get(1)
        # great_gatsby = Book(name = 'The Great Gatsby', author = a)
        # hobit = Book(name = 'The Hobbit', author = a)
        # godfather = Book(name = 'The GodFather', author = a)
        # john_doe = User(username = 'John Doe', password = 'abc')
        # jane_doe = User(username = 'Jane Doe', password = 'def')
        # db.session.add(hobit)
        # db.session.add(godfather)
        # db.session.add(john_doe)
        # db.session.add(jane_doe)
        # db.session.commit()

    ####create links between users and books####

        # john = db.session.query(User).get(1)
        # hobit = db.session.query(Book).get(2)
        # john_hobit = UsersBook(
        #     rating = 5.0,
        #     status = 'read'
        # )
        # john_hobit.user = john
        # john_hobit.book = hobit
        # db.session.add(john_hobit)

        # db.session.commit()

    # if True:
    #     john_doe = User.query.get(1)
    #     great_gatsby = Book.query.get(3)

    #     john_gatsby = UsersBook(rating = 1, status='read')
    #     john_gatsby.user = john_doe
    #     john_gatsby.book = great_gatsby

    #     db.session.add(john_gatsby)

    #     db.session.commit()


    # john_doe = User.query.get(1)

    # return '<br>'.join(list(map(
    #     lambda book: '{}: {}'.format(users_book.book.name, users_book.rating),
    #     john_doe.books
    # )))

    # return 'done'

