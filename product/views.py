from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def product_view(request):
    if request.method == 'GET':
        return HttpResponse('Product View')

def hello_view(request):
    return render(request, 'index.html')

def current_date_view(request):
    if request.method == 'GET':
        return HttpResponse('13.12.2023')

def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')
