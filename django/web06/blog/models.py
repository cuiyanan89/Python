from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    birthday = models.DateField(null=True)
    sex = models.CharField(max_length=1,choices=(('f','famale'),('m','male')))
    regist_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.username
