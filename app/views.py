from django.shortcuts import render, redirect
from .models import Task, User
from .forms import TaskForm
import sqlite3



DATABASE_NAME = 'bot/data.db'


def home(request):
    return render(request, 'index.html')

def get_users_from_bot_db():
    DATABASE_PATH = 'bot/data.db'
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT username, amount FROM users ORDER BY amount DESC')
    users = cursor.fetchall()
    conn.close()
    return users

def leaderboard(request):
    users = get_users_from_bot_db()
    # Prepare data for the template
    ranked_users = []
    for index, (username, amount) in enumerate(users):
        rank = index + 1 
        medal = ''
        if rank == 1:
            medal = '🥇'
        elif rank == 2:
            medal = '🥈'
        elif rank == 3:
            medal = '🥉'
        else:
            medal = f'#{rank}'
        ranked_users.append({'username': username, 'amount': amount, 'medal': medal})
    
    return render(request, 'leaderboard.html', {'users': ranked_users})


def friends(request):
    return render(request, 'friends.html')

def aref(request):
    return render(request, 'a_friends.html')

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks.html', {'form': form})

def remove_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.delete()
    return redirect('tasks')
