 
from flask import Flask, Response, request,  jsonify
from flask_restful import Resource
import json
from flask_jwt_extended import jwt_required, get_jwt_identity
import pandas as pd
from Main.Model.Skill import Skill, Project
from Main.Model.UserProjects import UserProjects
from Main.Model.User import User


class SkillApi(Resource):
    def get(self):
        skills = Skill.objects.all()
        leng = len(skills)
        data = []
        for i in range(leng):
            data.append({
                "skill_name": skills[i].skill_name,
                "skill_description": skills[i].skill_description,
                "priority": skills[i].priority,
            })
        return Response(json.dumps(data), mimetype='application/json')
    def post(self):
        data = request.get_json()
        nos = int(data['priority'])
        skill = Skill(**data).save()

        return {'Response:': 'Skill added sucessfully !!'}, 200
    def delete(self):
        data = request.get_json()
        skill = Skill.objects(skill_name=data['skill_name']).first()
        skill.delete()
        return {'Response:': 'Skill deleted sucessfully !!'}, 200


class Projects(Resource):
    @jwt_required()
    def post(self):
        username = get_jwt_identity()
        user = User.objects(username=username).first()
        body = request.get_json()
        name = body.pop('project_name')
        skill_name = body.pop('skills')

        skill_list = []
        for i  in skill_name:
            skill_list.append(Skill.objects(skill_name=i).first())
        body['skills'] = skill_list
        body['project_name']=name
        print(body)
        project = Project(**body).save()
        UserProjects(User=user, Project=project, Status=0).save()
        return {'Response:': 'Project added sucessfully !!'}, 200
    
    def get(self):
        body = request.get_json()
        name = body.pop('project_name')
        project = Project.objects(project_name=name).first()
        skills = project.skills
        skill_list = []
        for i in skills:
            skill_list.append(i.skill_name)
        body['skills'] = skill_list
        body['project_name']=name
        return Response(json.dumps(body), mimetype='application/json')

    def delete(self):
        data = request.get_json()
        project = Project.objects(project_name=data['project_name']).first()
        project.delete()
        return {'Response:': 'Project deleted sucessfully !!'}, 200

class UserProjectsAPI(Resource):
    
    @jwt_required()
    def get(self):
        username = get_jwt_identity()
        print(username)
        user = User.objects(username=username).first()
        user_projects = UserProjects.objects(User__in=[user.id]).all()

        data = []        
        for i in user_projects:
            project = i.Project
            skill = project.skills
            skill_list = []
            for i in skill:
                skill_list.append(i.skill_name)

            data.append({
                "project_name": project.project_name,
                "project_description": project.project_description,
                "project_reward": project.project_reward,
                "skills": skill_list,
            })
        return Response(json.dumps(data), mimetype='application/json')

    