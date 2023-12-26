# models.py

from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)

class Clothe(models.Model):
    image = models.ImageField(upload_to='clothe_images/')
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='clothes')

class Review(models.Model):
    clothe = models.ForeignKey(Clothe, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()

