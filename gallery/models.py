from django.db import models

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', default='null')
    # record=models.FileField(upload_to='documents/', default='null')
    def __str__(self):
        return self.title