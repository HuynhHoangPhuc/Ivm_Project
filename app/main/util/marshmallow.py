from flask_marshmallow import Marshmallow

marshmallow = Marshmallow()


def initialize_marshmallow(app):
    marshmallow.init_app(app)
