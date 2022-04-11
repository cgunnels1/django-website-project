from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=60)
    writer = models.CharField(max_length=60)
    #thumb = models.ImageField(default='default.jpg',blank=True)
    audioFile = models.FileField(upload_to='songs/', default='null')
    def __str__(self):
        return self.title

