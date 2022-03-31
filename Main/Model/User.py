from  Main.DAC.dbconfig import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Document):
    image = db.ImageField()
    username = db.StringField(required=True, unique=True)
    password = db.StringField()
    email = db.StringField(required=True, unique=True)
    name = db.StringField()

    def save_image(self,image):
        self.image.replace(image,filename=self.username)    

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)