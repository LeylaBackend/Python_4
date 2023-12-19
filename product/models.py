# Create your models here.

from django.db import models

class Clothe(models.Model):
    objects = None
    image = models.ImageField(upload_to='clothe', null=True, blank=True)
    title = models.CharField(max_length=350)
    text = models.TextField()
    price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


