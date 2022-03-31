from  Main.DAC.dbconfig import db

class Skill(db.Document):
    id = db.IntField(primary_key=True)
    skill_name = db.StringField( unique=True)
    skill_description = db.StringField()
    skill_level = db.IntField()
    def __repr__(self):
        return '<Skill {}>'.format(self.skill_name)



class Project(db.Document):
    id = db.IntField(primary_key = True)
    project_name = db.StringField( unique=True)
    project_description = db.StringField( unique=True)
    project_reward = db.IntegerField()
    skills = db.ListField(db.ReferenceField('Skill', reverse_delete_rule=db.PULL))
    def __repr__(self):
        return '<project {}>'.format(self.project_name)