from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import psycopg2
from psycopg2 import sql

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fjgsftzrdjovzuey'
    
    # Set the PostgreSQL connection URI for RDS (without the database name)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://demo_admin:m#xyb!4q<$WZV_w6W2QD]7Z3GbQ0@demo-env-db.cpxgsuaa8wqm.us-west-1.rds.amazonaws.com:5432'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional: Disable modification tracking for performance

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import models
    from .models import User, Task

    # Initialize database (This will connect to RDS, no need for local DB creation)
    create_database(app)

    # Setup login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    with app.app_context():
        # Connect to the RDS instance to check if the database exists
        conn = psycopg2.connect(
            dbname='postgres',  # Connect to the default maintenance database
            user='demo_admin',
            password='m#xyb!4q<$WZV_w6W2QD]7Z3GbQ0',
            host='demo-env-db.cpxgsuaa8wqm.us-west-1.rds.amazonaws.com',
            port='5432'
        )
        conn.autocommit = True  # Ensure database creation is immediately committed
        cursor = conn.cursor()
        
        # Check if the database exists
        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s;", ('flaskpostgre',))
        exists = cursor.fetchone()
        
        if not exists:
            # If database doesn't exist, create it
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier('flaskpostgre')))
            print("Database 'flaskpostgre' created on RDS!")

        # Close the cursor and connection after checking
        cursor.close()
        conn.close()

        # Now that the database exists, create the tables
        db.create_all()
        print('Database tables created on RDS!')