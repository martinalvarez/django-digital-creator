from django.db import models

# Create your models here.
class Albums(models.Model):
    name = models.CharField(max_length=255, null=False)
    release = models.DateField()
