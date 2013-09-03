from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    birthday = models.DateField(blank=True)
    headimg = models.FileField(upload_to='./images')
    desc = models.TextField(max_length=1000)
    sex = models.CharField(max_length=1,choices=(('m','male'),('f','famale')))

    def __unicode__(self):
        return self.username
