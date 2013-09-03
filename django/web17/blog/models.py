from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employ(models.Model):
    user = models.OneToOneField(User)
    tel = models.CharField(max_length=20)
    headimg = models.FileField(upload_to='./images')
