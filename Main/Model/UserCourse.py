from  Main.DAC.dbconfig import db
from flask_bcrypt import generate_password_hash, check_password_hash

class UserCourse(db.Document):
    User = db.ReferenceField('User', reverse_delete_rule=db.PULL)
    Course = db.ReferenceField('Course', reverse_delete_rule=db.PULL)
    Status = db.IntField(default=0)
