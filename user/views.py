# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from user.forms import RegisterForm

def register_view(request):
    if request.method == 'GET':
        context ={
            'form': RegisterForm,
        }

        return render(request, 'user/register.html', context=context)

    elif request.method == 'POST':
        print(request.POST)

        return HttpResponse(request.POST)