from flask import  url_for, request, render_template, make_response, flash, redirect
from flask import current_app as app
from flask_login import login_required, logout_user, current_user, login_user
from . import loginManager
from .auth import create_password, check_password
from .forms import LoginForm, RegistrationForm, BookAdditionForm
from .models import db, Book, Author, UsersBook, User


@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/list/')
@login_required
def list_of_books():
    """Creates a list of all books in database. User can browse list and choose a book from it."""

    return render_template('/list_of_all_books.html',
    all_books = Book.query.all())


@app.route('/profile')
@login_required
def profile():


    return render_template('/profile.html')


@app.route('/list/add-book', methods=('GET', 'POST'))
@login_required
def add_a_book():
    """Enables adding new books into db to a user. Checks for duplicates."""
    form=BookAdditionForm()

    if form.validate_on_submit():
        listed_book = Book.query.filter_by(name=form.name.data).first()
        existing_author = Author.query.filter_by(name=form.name.data).first()
        if listed_book:
            flash('This book is already in our database.')
            return redirect(url_for('list_of_books'))
        if existing_author:
            new_book = Book(
            name= form.name.data,
            author= existing_author,
            synopsis= form.synopsis.data,
            cover= form.cover.data
            )
            db.session.add(new_book)
            db.session.commit()
        else:
            new_book = Book(
                name= form.name.data,
                author= form.author.data,
                synopsis= form.synopsis.data,
                cover= form.cover.data
                #error = 'str' object has no attribute '_sa_instance_state'
                #probably colission in file(form) vs str(db) input?
            )
            new_author = Author(
                name= form.author.data
            )

            db.session.add(new_book)
            db.session.add(new_author)
            db.session.commit()
        
        flash('Book has been added.')
        return redirect(url_for('list_of_books'))
    return render_template('/add_a_book.html', form=form)



@app.route('/register', methods= ('GET', 'POST'))
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.data['username']).first()
        if existing_user:
            flash('User already exists. For loging in use our login page.')
            return redirect(url_for('login'))
        user = User(
            username = form.data['username'],
            password = create_password(form.password.data)
        )

        db.session.add(user)
        db.session.commit()

        login_user(user)

        flash('Your account was created')
        return redirect(url_for('profile'))
    return render_template('/registration.html', form=form)


@app.route('/login', methods= ('GET', 'POST'))
def login():
    """Log in for already existing user. Check if user and password
    match - redirect to user profile. Otherwise asks for new login."""
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.data['username']).first()

        if user is not None and check_password(form.data['password'], user.password):
            login_user(user, form.remember_me.data)

            flash('You have been logged in.')

            return redirect(url_for('profile'))
        else:
            flash('Incorrect username or password. Please try again.')

            return redirect(url_for('login'))

    return render_template('/login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    """Logs out current_user."""
    logout_user()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(_):
    """Creates own custom view for 404 error."""

    return make_response(
        render_template('/404.html'),
        404
    )


@loginManager.user_loader
def load_user(user_id):
    """Holds info of user in current session."""
    if user_id:
        return User.query.get(int(user_id))

    return None


@app.context_processor
def inject_user():
    """Inject data of current user into templates and forms."""

    return dict(
        user = current_user
    )


@app.route('/db')
def populatedb():
    """Populates db with fake data."""
### pass data here
