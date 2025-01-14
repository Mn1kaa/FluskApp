#Sirve para manejar  la creacion de la app desde afuera del main .py

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

from .auth import auth

from .config import Config


app= Flask(__name__)


app.config.from_object(Config)
db=SQLAlchemy(app)


from .members import members


def create_app():
    
    with app.app_context():
        db.create_all()
    bootsrap = Bootstrap(app)
    app.register_blueprint(auth)
    app.register_blueprint(members)

    return app


