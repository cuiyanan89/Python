from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=300)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

class Replay(models.Model):
    content = models. TextField(max_length=100)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return self.content
