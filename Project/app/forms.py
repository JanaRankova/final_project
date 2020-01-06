from flask_wtf import FlaskForm, Form
from wtforms import PasswordField, StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):

    username = StringField('Name', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField('Create an account')

class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')