from django.db import models

# Create your models here.
class new(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=30000)
    img = models.FileField(upload_to='./images')

    def __unicode__(self):
        return self.title
