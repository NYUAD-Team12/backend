 
from flask import Flask, Response, request,  jsonify
from flask_restful import Resource
import json
from Main.bot import bot
import pandas as pd
from Main.Model.Skill import Skill, Project
from Main.Model.UserCourse import UserCourse as UC
from Main.Model.User import User

class Userlesson(Resource):
    def get(self,username):
        user = User.objects(username=username).first()
        uc = UC.objects(User=user).all()
        leng = len(uc)
        data = []
        for i in range(leng):
            data.append({
                "name" : uc[i].Course.name,
                "title": uc[i].Course.title,
                "level" : uc[i].Course.level,
            })
        return Response(json.dumps(data), mimetype='application/json')

class SkillApi(Resource):
    def post(self):
        data = request.get_json()
        nos = int(data['level'])
        


        course = Course.objects(name=name).first()
        uc = UC.objects(User=user,Course=course).first()
        if not uc:
            return "Please register "
        if nos < 0:
            nos = 1
        uc.update(Status= int(nos))
        # return string sucessfully
        return Response("Success the current status of User is " + str(nos), mimetype='application/json')


class CourseApi(Resource):
    def get(self):
        # get list of all course
        course = Course.objects.all()
        leng = len(course)
        data = []
        for i in range(leng):
            data.append({
                "name": course[i].name,
                "title": course[i].title,
                "level": course[i].level,
            })
        return Response(json.dumps(data), mimetype='application/json')

class UpCourse(Resource):
    def post(self):
        body = request.get_json()
        username = body.pop('username')
        name = body.pop('name')
        user = User.objects(username=username).first()
        course = Course.objects(name=name).first()
        check = UC.objects(User=user,Course=course).first()
        if check:
            return "User already registered"
        UC(User = user, Course = course).save() 
        return {'Response:': user.username +' has been added to '+course.title}, 200

    def delete(self):
        body = request.get_json()
        username = body.pop('username')
        name = body.pop('name')
        user = User.objects(username=username).first()
        course = Course.objects(name=name).first()
        check = UC.objects(User=user,Course=course).first()
        if not check:
            return "User not registered"
        check.delete()
        return {'Response:': user.username +' has been removed from '+course.title}, 200


        

    