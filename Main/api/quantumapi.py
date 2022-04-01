from flask import Flask, Response, request, send_file
from Main.Model.Skill import Project
from Main.Model.Volunteer import VUser
from Main.Model.User import User
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
import json
from Main.api.utils.sim import main
class Quantumapi(Resource):
    def get(self):
        volunteers = VUser.objects.all()
        volunteer_dict = {}
        for i in volunteers:
            volunteer_dict[i.username] = i.skills
        print(volunteer_dict)
        jobs = Project.objects.all()
        job_dict = {}
        for i in jobs:
            job_dict[i.project_name] = (10, i.skills)
        print(job_dict)
        print(volunteer_dict)
        alocation = main(volunteer_dict, job_dict)
        return Response(json.dumps(alocation), mimetype='application/json')




