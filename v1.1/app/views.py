from django.shortcuts import render, redirect
from .models import User, Friend, Task
from .forms import TaskForm
import sqlite3
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User



DATABASE_NAME = 'bot/data.db'


from django.shortcuts import render, redirect
from .models import User, Friend

def leaderboard(request):
    user_id = request.session.get('user_id')
    
    user = User.objects.get(id=user_id)
    rank = User.objects.filter(coins__gt=user.coins).count() + 1
    
    context = {
        'user': user,
        'rank': rank,
    }
    return render(request, 'leaderboard.html', context)

def friends(request):
    user_id = request.session.get('user_id')
    friends = Friend.objects.filter(user_id=user_id)
    
    if friends.exists():
        return render(request, 'a_friends.html', {'friends': friends})
    else:
        return render(request, 'friends.html')

def home(request):
    user_id = request.GET.get('user_id')
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return render(request, '404.html', {})
    context = {
        'coins': user.coins,
    }
    return render(request, 'index.html', context)

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


