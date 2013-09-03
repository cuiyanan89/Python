from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    def __unicode__(self):
        return self.username

class Types(models.Model):
    foodtype = models.CharField(max_length=10)

    def __unicode__(self):
        return self.foodtype

class Foods(models.Model):
    foodname = models.CharField(max_length=20)
    fooddesc = models.CharField(max_length=500,blank=True)
    foodimg = models.FileField(upload_to='./images',blank=True)
    foodprice = models.DecimalField(max_digits=3,decimal_places=1)
    foodtype = models.ForeignKey(Types)

    def __unicode__(self):
        return self.foodname

class LineItem(models.Model):
    food = models.ForeignKey(Foods)
    quantity = models.IntegerField()

    def __unicode__(self):
        return self.food
