#coding:utf8
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(verbose_name=u'姓名',max_length=30)
    password = models.CharField(verbose_name=u'口令',max_length=100)
    email = models.EmailField(blank=True,null=True)
    birthday = models.DateField(blank=True,null=True)
    headimg = models.FileField(blank=True,upload_to='images',null=True)
    disc = models.TextField(blank=True,max_length=1000,null=True)

    def __unicode__(self):
        return self.username
