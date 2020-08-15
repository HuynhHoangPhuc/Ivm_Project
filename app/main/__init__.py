from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_restful import Api

from app.main.config import config_by_name

from app.main.model.db import initialize_db
from app.main.util.bcrypt import initialize_bcrypt
from app.main.util.marshmallow import initialize_marshmallow
from app.main.routes import initialize_routes


def create_app(config_name):
    app = Flask(__name__)
    api = Api(app)

    app.config.from_object(config_by_name[config_name])
    initialize_db(app)
    initialize_bcrypt(app)
    initialize_marshmallow(app)
    initialize_routes(api)

    return app
