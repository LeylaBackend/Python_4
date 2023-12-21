from django.contrib import admin

# Register your models here.

from product.models import Clothe, Categorie, Categories_type

admin.site.register(Clothe)

admin.site.register(Categorie)

admin.site.register(Categories_type)

