from django.urls import path

from product.views import main_view, products_list_view, \
    category_list_view, product_detail_view, product_create_view, category_create_view, product_update_view

urlpatterns = [
    path('', main_view),
    path('products/', products_list_view),
    path('category/', category_list_view),
    path('product/create/', product_create_view),
    path('products/<int:product_id>', product_detail_view),
    path('products/<int:product_id>/update/', product_update_view),
    path('category/create/', category_create_view),
]