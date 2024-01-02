from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from product.models import Clothe, Category, Review
from product.forms import ProductForm, CategoryForm, ReviewForm


def hello_view(request):
    return render(request, 'index.html')


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def products_list_view(request):
    if request.method == 'GET':
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

        return render(request, 'category/categories.html', context=context)


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
            'categories': categories,
            'review': review
        }

        return render(
            request,
            'products/detail.html',
            context=context
        )
    # elif request.method == 'POST':
    #     product = Clothe.objects.get(id=product_id)
    #
    #     # if form.is_valid():
    #     #     Review.objects.create(
    #     #         text=form.cleaned_data.get('text'),
    #     #         product=product
    #     #
    #     #     )
    #
    #     context = {
    #         'product': product,
    #         'review': product.reviews.all(),
    #     }
    #     return render(request, 'products/detail.html', context=context)


def product_create_view(requests, form=None):
    if requests.method == 'GET':
        context = {
            'form': ProductForm,
        }

        return render(requests, 'products/create.html', context=context)

    if requests.method == 'POST':
        form = ProductForm(requests.POST, requests.FILES)

        if form.is_valid():
            Clothe.objects.create(
                image=form.cleaned_data['image'],
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                price=form.cleaned_data['price'],
            )

        return redirect('/products/')

    context = {
        'form': form,
    }

    return render(requests, 'products/create.html', context=context)


def category_create_view(requests, form=None):
    if requests.method == 'GET':

        context = {
            'form': CategoryForm,
        }

        return render(requests, 'category/create.html', context=context)

    elif requests.method == 'POST':
        form = CategoryForm(requests.POST)

        if form.is_valid():
            Category.objects.create(
                title=form.cleaned_data['title'],
            )

        return redirect('/category/')

    context = {
        'form': form,
    }

    return render(requests, 'category/create.html', context=context)

def review_product_view(request):
    if request.method == 'GET':
        context = {
            'form': ReviewForm
        }
        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products')
        else:
            context = {
                'form': form

            }
            return render(request, 'products/detail.html', context=context)


