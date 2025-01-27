from website import create_app, db
from website.models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def migrate_user():
    # Create user data
    user_data = User(
        email='victoria.ripardo@ezops.cloud',
        password='scrypt:32768:8:1$bnh24v7ygbmgqtwd$7eb7ddb7e07d742a167f70feb9a55d0824679d341fee00ff305adc895202bcdd36d4e203e10dada6fd757ef228e6e9f483468099a018fcf2a1bf996b057b0349',
        first_name='Vika Ripardo'
    )
    
    # Get Flask app context
    app = create_app()
    with app.app_context():
        # Add and commit the user
        db.session.add(user_data)
        db.session.commit()
        print("User migrated successfully!")

if __name__ == '__main__':
    migrate_user()
