from Main.api.userapi import UserApi, UsersApi, UserImageApi
from Main.api.authapi import SignupApi, LoginApi
from Main.api.skill import SkillApi, Projects, UserProjectsAPI

def initialize_routes(api):
    # List users
    api.add_resource(UsersApi, '/api/vol') 
    api.add_resource(UserApi, '/api/user')
    api.add_resource(UserImageApi, '/api/user/image')
    # Auth
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

    # Skills
    api.add_resource(SkillApi, '/api/skill')
    api.add_resource(Projects, '/api/project')
    api.add_resource(UserProjectsAPI, '/api/user/project')

