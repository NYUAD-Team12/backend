from  Main.DAC.dbconfig import db
from flask_bcrypt import generate_password_hash, check_password_hash

class VUser(db.Document):
    username = db.StringField(required=True, unique=True)
    email = db.StringField(required=True)
    name = db.StringField()
    skills = db.DictField()


    def save_image(self,image):
        self.image.replace(image,filename=self.username)    

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)