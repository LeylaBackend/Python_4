from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.

def product_view(request):
    if request.method == 'GET':
        return HttpResponse('Product View')

def hello_view(request):
    return render(request, 'index.html')

def current_date_view(request):
    current_date = timezone.now().date()
    return HttpResponse(f'Current Date: {current_date}')

def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')
