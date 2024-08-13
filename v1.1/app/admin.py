from django.contrib import admin
from .models import Task, User

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'points', 'button_link')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'name', 'amount', 'invited_friends')
