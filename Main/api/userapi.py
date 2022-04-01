from flask import Flask, Response, request, send_file
from flask_mongoengine import json
from Main.Model.Volunteer import VUser
from Main.Model.User import User
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
import json

class UsersApi(Resource):
  
  def get(self):
    # get all users
    users = VUser.objects.all()
    leng = len(users) 
    data = []
    for i in range(leng):
      data.append({
        "username": users[i].username,
        "email": users[i].email,
        "name": users[i].name,
        "skills": users[i].skills,
      })
    return Response(json.dumps(data), mimetype='application/json')
  
  def post(self):
    body = request.get_json()   
    user = VUser(**body).save()
    return {'user': user.username}, 200
  

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