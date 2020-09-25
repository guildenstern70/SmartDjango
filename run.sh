#!/bin/bash
#
# SmartDjango Python Project
#
# Copyright (c) 2020 Alessio Saltarin
# This software is distributed under MIT License.
# See LICENSE.
#
#

echo "make migrations"
python manage.py makemigrations
echo "migrate"
python manage.py migrate
echo [$0] Starting GUnicorn Server...
exec gunicorn -w 3 SmartDjango.wsgi:application --bind 0.0.0.0:8080


