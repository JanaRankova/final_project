from flask_wtf import FlaskForm, Form
from wtforms import PasswordField, StringField, SubmitField, BooleanField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, Optional
from .models import User

class RegistrationForm(FlaskForm):

    username = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Re-enter password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create an Account')

class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class BookAdditionForm(FlaskForm):

    name=StringField('Title', validators=[DataRequired()])
    author=StringField('Author', validators=[DataRequired()])
    synopsis=TextAreaField('Synopsis', validators=[Optional(), Length(max=500)])
    cover=FileField('Book Cover', validators=[Optional()])
    submit=SubmitField('Add This Book')
