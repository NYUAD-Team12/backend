from flask import Flask, Response, request, send_file
from flask_mongoengine import json
from Main.Model.Skill import Project
from Main.Model.Volunteer import VUser
from Main.Model.User import User
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
import json

class Quantapi(Resource):
    def post():
        volunteers = VUser.objects.all()
        volunteer_dict = {}
        for i in volunteers:
            volunteer_dict[i.username] = i.skills
        jobs = Project.objects.all()
        job_dict = {}
        for i in jobs:
            job_dict[i.project_name] = i.skills
        return volunteer_dict


