from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    return render(request, 'main.html')


@login_required
def status(request):
    return HttpResponse('Some status OK text<a href ="/">Home</a> ')


def auth(request):
    return render(request, 'auth.html')


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def profile(request):
    current_user = request.user
    if request.method == 'POST':

        current_user.first_name = request.POST.get('first_name')
        current_user.last_name = request.POST.get('last_name')
        current_user.info = request.POST.get('info')
        current_user.save()
        # photo = request.POST.get('photo')


    first_name = current_user.first_name
    last_name = current_user.last_name
    # info = current_user.info  # fix this field
    print(first_name, last_name, current_user)

    return render(request, 'profile.html', {'context': {'first_name': first_name,
                                             'last_name': last_name}})
