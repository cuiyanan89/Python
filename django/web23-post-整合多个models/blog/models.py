from django.db import models
from django.contrib.auth.models import User

class ProUser(models.Model):
    user=models.OneToOneField(User)
    tel=models.CharField(max_length=16)
    headimg=models.FileField(upload_to='./pet')
