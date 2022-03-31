from flask import Flask, Response, request, send_file
from flask_mongoengine import json
from Main.Model.User import User
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
import json

class UsersApi(Resource):
  
  def get(self,username):
    #check if user exsist
    user = User.objects(username=username).first()
    if user:
      return Response("0")
    else:
      return Response("1")  
  
  def post(self,username):
    body = request.get_json()
    user = User(**body).save()
    id = user.id
    return {'id': str(id)}, 200

class Checkemail(Resource):

  def get(self,email):
    user = User.objects(email=email).first()
    print(user)
    if user:
        return Response("1")
    else:
        return Response("0")  

  

class UserApi(Resource):
  
  @jwt_required()
  def put(self):
    username = get_jwt_identity()
    body = request.get_json()
    user = User.objects(username=username)
    if 'image' in request.files:
      image = request.files['image']
      user.save_image(request.files['image'])
    user.update(**body)
    return '', 200
  
  @jwt_required()
  def delete(self):
    username = get_jwt_identity()
    user = User.objects.get(username=username).delete()
    return '', 200
  
  @jwt_required()
  def get(self):
    username = get_jwt_identity()
    user = User.objects(username=username).to_json()
    # remove the _id field
    user = json.loads(user)
    user = user[0]
    del user["_id"]
    del user["image"]
    return Response(json.dumps(user), mimetype="application/json", status=200)
    
class UserImageApi(Resource):
  '''
  Retreieve and send user image
  '''
  @jwt_required()
  def get(self):
    username = get_jwt_identity()
    user = User.objects(username=username).first()
    image = user.image
    print(type(image))
    return send_file(image, mimetype='image/png')