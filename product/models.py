# Create your models here.

from django.db import models



class Categories_type(models.Model):
    title = models.CharField(max_length=350, null=True, blank=True, verbose_name='Текст')
    # created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    # updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self) -> str:
        return f"{self.title}"




class Clothe(models.Model):
    objects = None
    image = models.ImageField(upload_to='clothe', null=True, blank=True)
    title = models.CharField(max_length=350, verbose_name="Заголовок")
    text = models.TextField(null=True, blank=True, verbose_name='Текст')
    price = models.FloatField(default=0.0, verbose_name='Рейтинг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(
        Categories_type,
        verbose_name='Категория',
        related_name='products'
    )

    def __str__(self) -> str:
        return f"{self.title}"

class Categorie(models.Model):
    objects = None
    product = models.ForeignKey("product.Clothe", on_delete=models.CASCADE, verbose_name="Пост", related_name="categories")
    text = models.TextField(null=True, blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')