"""This is init module."""
from flask_restful import Api
from flask import Flask
from flask_bcrypt import Bcrypt
import os
from Main.Routes.routes import initialize_routes
from flask_jwt_extended import JWTManager
from config import Config
from flask_cors import CORS, cross_origin
# Place where app is defined
app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)
CORS(app, resources=r'/api/*',allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Methods"])
#CORS(app)
DB = "mongodb+srv://AnushAdmin:29M0UfeC1YZvEMjr@cluster0.0p0ix.mongodb.net/nyu"

app.config['MONGODB_SETTINGS'] = {
    'host': DB
}
jwt = JWTManager(app)

from Main.DAC.dbconfig import initialize_db
initialize_db(app)
initialize_routes(api)
bcrypt = Bcrypt(app)

