# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from user.forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == 'GET':
        context ={
            'form': RegisterForm,
        }

        return render(request, 'user/register.html', context=context)

    elif request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                password=form.cleaned_data.get('password')
            )

            return redirect('/auth/login/')

        else:
            context = {
                'form': form,
            }

            return render(request, 'user/register.html', context=context)


def login_view(request):
    if request.method == 'GET':
        context = {
            'form': LoginForm,
        }
        print(request.user)  #
        return render(request, 'user/login.html', context=context)

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(**form.cleaned_data)

            if user is not None:
                login(request, user)
                return redirect('/products/')

            else:
                form.add_error(
                    None,
                    'Пользователь с такими данными не найден!'
                )

        return render(request, 'user/login.html', context={'form': form})

def logout_view(request):
    logout(request)
    return redirect('/products/')

def profile_view(request):
    if request.method == 'GET':
        context = {
            'user': request.user,
        }

        return render(request, 'user/profile.html', context=context)

