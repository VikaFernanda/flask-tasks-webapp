# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

class Config:
    SECRET_KEY = '1b1a0de2fa29ad0844a4a92dfbca7d1af2132909ef02f4549f6dba6292f5e071'
    SQLALCHEMY_DATABASE_URI = 'postgresql://flask_admin:yGmgKJ!7MVG9gjQq@flaskwebapp.cpxgsuaa8wqm.us-west-1.rds.amazonaws.com/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False