from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/remove/<int:task_id>/', views.remove_task, name='remove_task'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('friends/', views.friends, name='friends'),
    path('aref/', views.aref, name='aref')
]
