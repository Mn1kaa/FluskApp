#Sirve para manejar  la creacion de la app desde afuera del main .py

from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from .auth import auth
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)


def create_app():
    
    bootsrap = Bootstrap(app)
    app.register_blueprint(auth)

    return app

