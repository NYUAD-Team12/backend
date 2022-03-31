from Main.api.userapi import UserApi, UsersApi, UserImageApi, Checkemail

from Main.api.authapi import SignupApi, LoginApi


class testApi(Resource):
    def get(self):
        return "test"
def initialize_routes(api):
    # List users
    api.add_resource(testApi, '/')
    api.add_resource(UsersApi, '/api/check/<username>') 
    api.add_resource(Checkemail, '/api/check/mail/<email>') 
    api.add_resource(UserApi, '/api/user')
    api.add_resource(UserImageApi, '/api/user/image')
    # Auth
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

