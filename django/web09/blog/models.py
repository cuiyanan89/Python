from django.db import models

# Create your models here.
class Nav(models.Model):
    name = models.CharField(max_length=10)


    def __unicode__(self):
        return self.name
class New(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date = models.DateField()
    img = models.FileField(upload_to='./newing')
    nav = models.ForeignKey(Nav)


    def __unicode__(self):
        return self.title[0:10]
