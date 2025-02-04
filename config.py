import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '1b1a0de2fa29ad0844a4a92dfbca7d1af2132909ef02f4549f6dba6292f5e071')
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority')