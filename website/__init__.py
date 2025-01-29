from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fjgsftzrdjovzuey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://demo_admin:m#xyb!4q<$WZV_w6W2QD]7Z3GbQ0@demo-env-db.cpxgsuaa8wqm.us-west-1.rds.amazonaws.com:5432/demo_db'
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Task
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    with app.app_context():
        db.create_all()
        print('Database tables created!')