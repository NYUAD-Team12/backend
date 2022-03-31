from  Main.DAC.dbconfig import db
from flask_bcrypt import generate_password_hash, check_password_hash

class UserProjects(db.Document):
    User = db.ReferenceField('User', reverse_delete_rule=db.PULL)
    Project = db.ReferenceField('Project', reverse_delete_rule=db.PULL)
    Status = db.IntField(default=0)

    def __repr__(self):
        return '<UserProjects {}>'.format(self.User.username)
