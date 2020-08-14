from app.main.controller.user_controller import UsersApi, UserApi


def initialize_routes(api):
    api.add_resource(UsersApi, '/api/movies')
    api.add_resource(UserApi, '/api/movies/<id>')
