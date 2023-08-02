#  SmartDjango Python Project
#
#  Copyright (c) 2021-23 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

import logging
from SmartDjango.forms import CustomUserCreationForm, CarForm
from SmartDjango.models import Car
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings as django_settings

logger = logging.getLogger(__name__)

def get_db_name():
    db_name = django_settings.DATABASES['default']['NAME']
    if db_name.endswith('sqlite3'):
        db_name = 'sqlite3'
    return db_name

def index(request):
    template = loader.get_template('index.html')
    context = {
        'title': 'SmartDjango',
        'version': '0.1'
    }
    return HttpResponse(template.render(context, request))


def loginform(request):
    logger.info('Login form.')
    errors = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        logger.info('Received login form POST')
        logger.info('Username = ' + username)
        user = authenticate(username=username, password=password)
        if user is not None:
            logger.info('User ' + username + ' was authenticated.')
            login(request, user)
            return HttpResponseRedirect('/home/')
        else:
            logger.info('User ' + username + ' is unknown or input wrong password.')
            errors = True
    template = loader.get_template('account/login.html')
    context = {
        'title': 'Login',
        'header': 'Login',
        'errors': errors
    }
    return HttpResponse(template.render(context, request))


def registration(request):
    template = loader.get_template('account/registration.html')
    if request.method == 'POST':
        newcar_form = UserCreationForm(request.POST)
        logger.info('Received registration data...')
        if newcar_form.is_valid():
            registered_user = newcar_form.cleaned_data['username']
            logger.info('Registration data is valid for user ' +
                        registered_user)
            newcar_form.save()
            return HttpResponseRedirect('/registered/' + registered_user)
        else:
            messages.error(request, newcar_form.errors)
            logger.info('Registration data is NOT valid')
    context = {
        'title': 'Registration',
        'header': 'Register new user',
        'form': CustomUserCreationForm(),
        'db_name': get_db_name()
    }
    return HttpResponse(template.render(context, request))


def registration_ok(request, username):
    logger.info('Showing registration info for user ' + username)
    template = loader.get_template('account/registration_ok.html')
    context = {
        'title': 'Registration',
        'header': 'User registered',
        'username': username,
        'db_name': get_db_name()
    }
    return HttpResponse(template.render(context, request))


@login_required
def home(request):
    template = loader.get_template('homepage.html')
    context = {
        'title': 'Homepage',
        'username': request.user.username,
        'db_name': get_db_name()
    }
    return HttpResponse(template.render(context, request))


@login_required
def cars(request):
    template = loader.get_template('cars.html')
    if request.method == 'POST':
        registration_data = CarForm(request.POST)
        logger.info('Received new car data...')
        if registration_data.is_valid():
            registration_data.save()
            return HttpResponseRedirect('/cars')
        else:
            messages.error(request, registration_data.errors)
            logger.info('New car data is NOT valid')
    context = {
        'title': 'Cars',
        'username': request.user.username,
        'cars': Car.objects.all(),
        'form': CarForm(),
        'db_name': get_db_name()
    }
    return HttpResponse(template.render(context, request))

@login_required
def delete_car(request, car_id):
    logger.info('Deleting car ' + str(car_id))
    Car.objects.filter(id=car_id).delete()
    return HttpResponseRedirect('/cars')

@login_required
def another(request):
    template = loader.get_template('anotherpage.html')
    title = request.GET.get('title', 'Another page')
    context = {
        'username': request.user.username,
        'title': title,
        'db_name': get_db_name()
    }
    return HttpResponse(template.render(context, request))


@login_required
def logout_view(request):
    logger.info('Logging out user ' + str(request.user))
    logout(request)
    return HttpResponseRedirect('/')



