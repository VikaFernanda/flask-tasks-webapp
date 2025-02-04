# import os
# from dotenv import load_dotenv
from urllib.parse import quote_plus

# # Load environment variables
# load_dotenv()

class Config:
    SECRET_KEY = '1b1a0de2fa29ad0844a4a92dfbca7d1af2132909ef02f4549f6dba6292f5e071'
    PASSWORD = quote_plus("m#xyb!4q<$WZV_w6W2QD]7Z3GbQ0")  # Encode special characters
    SQLALCHEMY_DATABASE_URI = f'postgresql://demo_admin:{PASSWORD}@demo-env-db.cpxgsuaa8wqm.us-west-1.rds.amazonaws.com/demodb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False