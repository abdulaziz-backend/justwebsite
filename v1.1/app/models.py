from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    points = models.IntegerField()
    button_link = models.URLField()

    def __str__(self):
        return self.title


class User(models.Model):
    user_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    invited_friends = models.IntegerField(default=0)
    invited_friends_usernames = models.TextField(default='[]')
    coins = models.IntegerField(default=0) 

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    coins = models.IntegerField(default=0)
    
    
class Friend(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='friends')
    friend = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_friends')
