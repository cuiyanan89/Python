from django.db import models

# Create your models here.
class New(models.Model):
    new_title = models.CharField(max_length=30)
    new_content = models.TextField(max_length=1000)
    new_img = models.FileField(upload_to='./images')

    def __unicode__(self):
        return self.new_title
