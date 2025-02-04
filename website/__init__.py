import os
from flask import Flask
from flask_login import LoginManager
from flask_mongoengine import MongoEngine
from config import Config

# Initialize MongoDB
db = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize MongoDB with the app
    db.init_app(app)

    # Import models AFTER initializing db
    from .models import User, Task  

    # Register blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Setup Login Manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.objects(id=user_id).first()  # MongoDB query

    return app