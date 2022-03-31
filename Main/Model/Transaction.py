from  Main.DAC.dbconfig import db
from flask_bcrypt import generate_password_hash, check_password_hash


class Transaction(db.Document):
    Tdate = db.StringField(required=True)
    amount = db.FloatField(required=True)
    category = db.StringField(required=True)
    description = db.StringField(required=True)
    currency = db.StringField(default="USD")