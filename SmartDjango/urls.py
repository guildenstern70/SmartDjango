#  SmartDjango Python Project
#
#  Copyright (c) 2021 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

#
#  SmartDjango Python Project
#
#


from django.contrib import admin
from django.urls import path

from SmartDjango import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('another/', views.another, name='another'),
    path('login/', views.loginform, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
]
