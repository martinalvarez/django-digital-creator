from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=255, null=False)

class Album(models.Model):
    artist = models.ForeignKey(Artist, null=False, on_delete=models.CASCADE)    
    name = models.CharField(max_length=255, null=False)
    release = models.PositiveSmallIntegerField()

