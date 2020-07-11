from django.db import models

# Create your models here.

class Job(models.Model):
    objects = models.Manager()
    image = models.ImageField(upload_to='image/')
    summary= models.CharField(max_length=200)