#
#  SmartDjango Python Project
#
#  Copyright (c) 2020 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
import logging

logger = logging.getLogger(__name__)


def index(request):
    template = loader.get_template('index.html')
    context = {
        'title': 'SmartDjango',
    }
    return HttpResponse(template.render(context, request))


@login_required
def another(request):
    template = loader.get_template('anotherpage.html')
    context = {
        'username': request.session['logged_user'],
        'title': 'Another Page',
    }
    return HttpResponse(template.render(context, request))


@login_required
def logout_view(request):
    logger.info('Logging out user ' + request.user)
    logout(request)
    return HttpResponseRedirect('/index/')


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
    template = loader.get_template('login.html')
    context = {
        'title': 'Login',
        'errors': errors
    }
    return HttpResponse(template.render(context, request))


@login_required
def home(request):
    template = loader.get_template('homepage.html')
    context = {
        'title': 'Homepage',
        'username': request.user.username,
    }
    return HttpResponse(template.render(context, request))
