import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Sets configuration variables for Flask."""

    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    #Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True