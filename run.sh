#!/bin/bash
#
# SmartDjango Python Project
#
# Copyright (c) 2020 Alessio Saltarin
# This software is distributed under MIT License.
# See LICENSE.
#
#
# export DJANGO_SETTINGS_MODULE=SmartDjango.realsettings
echo "make migrations"
python manage.py makemigrations
echo "migrate"
python manage.py migrate
echo [$0] Starting Django Server...
python manage.py runserver


