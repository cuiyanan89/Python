#coding:utf8
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(verbose_name=u'姓名',max_length=20)
    password = models.CharField(verbose_name=u'密码',max_length=100)

    def __unicode__(self):
        return self.username

class Foodtype(models.Model):
    foodtype = models.CharField(max_length=10)
    def __unicode__(self):
        return self.foodtype

class Food(models.Model):
    foodname = models.CharField(max_length=30)
    foodimg = models.FileField(upload_to='./images')
    foodprice = models.CharField(max_length=3)
    foodtype = models.ForeignKey(Foodtype)
    def __unicode__(self):
        return self.foodname

