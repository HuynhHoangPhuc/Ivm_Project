from flask import Response, request
from flask_restful import Resource


from app.main.service.user_service import *


class UsersApi(Resource):
    def get(self):
        users = get_all_users
        return Response(users, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        return create_a_user(**body)


class UserApi(Resource):
    def put(self, uuid):
        body = request.get_json()
        return update_a_user(uuid, **body)

    def delete(self, uuid):
        return delete_a_user(uuid)

    def get(self, uuid):
        user = get_a_user(uuid)
        return Response(user, mimetype="application/json", status=200)
