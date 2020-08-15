from app.main.util.marshmallow import marshmallow
from app.main.model.user import User


class UserSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = User

    email = marshmallow.auto_field()
    phone = marshmallow.auto_field()
    registered_on = marshmallow.auto_field()
