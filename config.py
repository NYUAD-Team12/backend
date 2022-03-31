import os

class Config:
    DB = os.environ.get('DB')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    #IBM_API = os.environ.get('IBM_API')
    Bname = os.environ.get('BLOB_NAME')
    Bkey = os.environ.get('BLOB_KEY')

    