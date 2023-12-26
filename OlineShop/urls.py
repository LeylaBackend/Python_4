"""
URL configuration for OlineShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from product.views import hello_view, current_date_view, goodbye_view, main_view, products_list_view, category_list_view, product_detail_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('product/', product_view),
    path('hello/', hello_view),
    path('current_date/', current_date_view),
    path('goodbye/', goodbye_view),
    path('', main_view),
    path('products/', products_list_view),
    path('catogory/', category_list_view),
    path('products/<int:product_id>', product_detail_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
