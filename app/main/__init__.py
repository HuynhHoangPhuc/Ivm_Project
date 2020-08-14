from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_restful import Api

from .config import config_by_name

from app.main.routes import initialize_routes

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    bcrypt.init_app(app)

    api = Api(app)
    initialize_routes(api)

    return app
