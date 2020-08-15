from app.main.controller.user_controller import UsersApi, UserApi


def initialize_routes(api):
    api.add_resource(UsersApi, '/api/users')
    api.add_resource(UserApi, '/api/users/<uuid>')
