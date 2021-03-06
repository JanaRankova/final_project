import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
loginManager = LoginManager()
csrf = CSRFProtect()


def create_app():
    """Innitiate app with databases and loginManager, sets up config."""

    app = Flask(
        __name__, instance_relative_config=False, static_folder='static'
    )
    app.config.from_object('config.Config')

    db.init_app(app)
    loginManager.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

        return app
