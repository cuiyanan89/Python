from django.db import models

# Create your models here.
class Picture(models.Model):
    pic_title = models.CharField(max_length=30)
    pic_file = models.FileField(upload_to='./upload')


    def __unicode__(self):
        return self.pic_title
