from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Task
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        task = request.form.get('task')
        
        if len(task) < 1:
            flash('Task description is too short', category='error')
        else:
            new_task = Task(text=task, user=current_user)  # Reference to User object
            new_task.save()  # Save to MongoDB
            flash('Task added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-task', methods=['POST'])
@login_required
def delete_task():
    task_data = json.loads(request.data)
    taskId = task_data['taskId']
    task = Task.objects(id=taskId).first()  # MongoDB query

    if task and task.user == current_user:  # Check task ownership
        task.delete()
        return jsonify({})

@views.route('/toggle-task', methods=['POST'])
@login_required
def toggle_task():
    task_data = json.loads(request.data)
    taskId = task_data['taskId']
    task = Task.objects(id=taskId).first()  # MongoDB query

    if task and task.user == current_user:  # Check task ownership
        task.is_done = task_data['isDone']
        task.save()  # Update MongoDB document

    return jsonify({})