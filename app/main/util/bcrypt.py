from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def initialize_bcrypt(app):
    bcrypt.init_app(app)
