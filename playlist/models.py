from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=60)
    writer = models.CharField(max_length=60)
    thumb = models.ImageField(default='default.jpg',blank=True)
    # record=models.FileField(upload_to='documents/', default='null')
    def __str__(self):
        return self.title

# class Audio_store(models.Model):
#     record = models.FileField(upload_to='documents/')
#     class Meta:
#         db_table='Audio_store'
