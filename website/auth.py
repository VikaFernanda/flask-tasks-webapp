from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')
    
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        # Check if the email already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        
        # Validate input
        elif len(email) < 4:
            flash('Email must be a valid one.', category='error')
        elif len(first_name) < 4:
            flash('First Name should be greater than 4 characters.', category='error')
        elif password2 != password1:
            flash('Passwords must be the same.', category='error')
        elif len(password1) < 5:
            flash('Password must be greater than 5 characters.', category='error')
        else:
            # Create new user and hash the password
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='scrypt'))
            
            # Save new user to the database
            db.session.add(new_user)
            db.session.commit()

            # Log the user in after account creation
            login_user(new_user, remember=True)
            flash('Account created successfully!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)
