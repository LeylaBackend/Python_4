from django.contrib import admin

# Register your models here.

from product.models import Clothe, Category, Review

admin.site.register(Clothe)

admin.site.register(Category)


admin.site.register(Review)
