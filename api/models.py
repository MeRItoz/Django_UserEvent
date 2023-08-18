# api/models.py

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')

class Collaborator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
