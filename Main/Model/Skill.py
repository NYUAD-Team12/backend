from  Main.DAC.dbconfig import db

class Skill(db.Document):
    skill_name = db.StringField( unique=True)
    skill_description = db.StringField()
    def __repr__(self):
        return '<Skill {}>'.format(self.skill_name)



class Project(db.Document):
    project_name = db.StringField( unique=True)
    project_description = db.StringField()
    project_reward = db.IntField()
    skills = db.DictField()
    def __repr__(self):
        return '<project {}>'.format(self.project_name)