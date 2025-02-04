import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Load environment variables
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '1b1a0de2fa29ad0844a4a92dfbca7d1af2132909ef02f4549f6dba6292f5e071')
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://vika-admin:wRuRUEaRM53MMhPG@flaskdb.ighkt.mongodb.net/?retryWrites=true&w=majority&appName=flaskdb')
    
# Create a new client and connect to the server
client = MongoClient(Config.MONGO_URI, server_api=ServerApi('1'))