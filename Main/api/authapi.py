from flask import request
from Main.Model.User import User
from flask_restful import Resource
from flask import Response, request
from flask_jwt_extended import create_access_token
import datetime

class SignupApi(Resource):
  def post(self):
    body = request.get_json()
    user = User(**body)
    # if body has password 
    if body.get('password'):
        user.hash_password()
    if 'image' in request.files:
      image = request.files['image']
      user.save_image(request.files['image'])
    user.save()
    data = {'id': str(user.username)}
    return data, 200

  

class LoginApi(Resource):
  def post(self):
   body = request.get_json()
   user = User.objects.get(username=body.get('username'))
   authorized = user.check_password(body.get('password'))
   if not authorized:
     return {'error': 'Email or password invalid'}, 401
   expires = datetime.timedelta(days=7)
   access_token = create_access_token(identity=str(user.username), expires_delta=expires)
   return {'token': access_token}, 200
  


