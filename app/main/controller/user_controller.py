from flask_restful import Resource, reqparse


from app.main.service.user_service import *


class UsersApi(Resource):
    def get(self):
        return get_all_users()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email")
        parser.add_argument("phone")
        parser.add_argument("password")
        user = parser.parse_args()
        return add_a_user(**user)


class UserApi(Resource):
    def put(self, uuid):
        parser = reqparse.RequestParser()
        parser.add_argument("email")
        parser.add_argument("phone")
        parser.add_argument("password")
        user = parser.parse_args()
        return update_a_user(uuid, **user)

    def delete(self, uuid):
        return delete_a_user(uuid)

    def get(self, uuid):
        return get_a_user(uuid)
