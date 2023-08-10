from django.db import models
from datetime import datetime

class room(models.Model):
    roomname=models.CharField(max_length=100)

class message(models.Model):
    value=models.CharField(max_length=1000)
    date=models.DateTimeField(default=datetime.now,blank=True)
    user=models.CharField(max_length=100)
    room=models.CharField(max_length=100)
