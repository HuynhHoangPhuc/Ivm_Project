import uuid
import datetime
import json

from app.main.model.db import db
from app.main.model.user import User
from app.main.schema.user_schema import UserSchema


def add_a_user(**data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            uuid=str(uuid.uuid4()),
            email=data['email'],
            phone=data['phone'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(new_user)
        db.session.commit()

        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    users = []
    for user in User.query.all():
        users.append(UserSchema().dump(user))
    return users


def get_a_user(uuid):
    user = User.query.filter_by(uuid=uuid).first()
    return UserSchema().dump(user)


def update_a_user(uuid, **data):
    user = User.query.filter_by(uuid=uuid).first()
    if user:
        user.email = data['email']
        user.phone = data['phone']
        user.password = data['password']
        db.session.add(user)
        db.session.commit()

        response_object = {
            'status': 'success',
            'message': 'Successfully updated.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User not already exists.'
        }
        return response_object, 409


def delete_a_user(uuid):
    user = User.query.filter_by(uuid=uuid).first()
    db.session.delete(user)
    db.session.commit()

    return 'Deleted'
