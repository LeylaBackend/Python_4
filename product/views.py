from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from product.models import Clothe, Category, Review


# Create your views here.

# def product_view(request):
#     if request.method == 'GET':
#         return HttpResponse('Product View')

def hello_view(request):
    return render(request, 'index.html')


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def products_list_view(request):
    if request.method == 'GET':
        products = Clothe.objects.all()

        context = {
            'products': products
        }

    return render(request, 'products/products.html', context=context)


def current_date_view(request):
    current_date = timezone.now().date()
    return HttpResponse(f'Current Date: {current_date}')


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')


def category_list_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        context = {
            'categories': categories,
        }

        return render(request, 'categories.html', context=context)

def product_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            clothe = Clothe.objects.get(id=product_id)
            categories = clothe.categories.all()
            review = Review.objects.all()
        except Clothe.DoesNotExist:
            return render(request, '404.html')

        context = {
            'clothe': clothe,
            'categories': categories,  # Pass the categories associated with the clothe
            'reviews': review
        }

        return render(
            request,
            'products/detail.html',
            context=context
        )