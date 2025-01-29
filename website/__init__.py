import boto3
import json
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

DB_NAME = "database.db"

def get_database_password(secret_arn):
    """Retrieve the database password securely from AWS Secrets Manager."""
    client = boto3.client('secretsmanager', region_name="us-west-1")

    try:
        response = client.get_secret_value(SecretId=secret_arn)
        secret_data = json.loads(response['SecretString'])
        return secret_data.get("password")  # Extract password from Secrets Manager response
    except Exception as e:
        print(f"Error retrieving secret: {e}")
        return None

def create_app():
    app = Flask(__name__)

    # AWS RDS Database Credentials
    rds_endpoint = "demo-env-db.cpxgsuaa8wqm.us-west-1.rds.amazonaws.com:5432"
    rds_username = "demo_user"
    secret_arn = "arn:aws:secretsmanager:us-west-1:975635808270:secret:rds!db-a9c387d0-70ff-4fa0-8185-73d438c7babf-evYPyw"

    # Retrieve the database password securely
    rds_password = get_database_password(secret_arn)
    if not rds_password:
        raise ValueError("Failed to retrieve database password.")

    # Application Configuration
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'fjgsftzrdjovzuey')  # Allow setting via env variable
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{rds_username}:{rds_password}@{rds_endpoint}/flaskpostgre'

    # Initialize Extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import models before database creation
    from .models import User, Task
    create_database(app)

    # User Authentication Handling
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    """Ensure that the database tables are created."""
    with app.app_context():
        db.create_all()
        print('Database tables created!')