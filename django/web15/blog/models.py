from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)

    def __unicode__(self):
        return self.title

class Replay(models.Model):
    title = models.CharField(max_length=20)

    def __unicode__(self):
        return self.title
