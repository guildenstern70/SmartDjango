#!/bin/bash
#
# SmartDjango Python Project
#
# Copyright (c) 2021-23 Alessio Saltarin
# This software is distributed under MIT License.
# See LICENSE.
#
#
if [ -z "${DJANGO_SUPERUSER_USERNAME}" ]; then
    export DJANGO_SUPERUSER_USERNAME='admin'
    export DJANGO_SUPERUSER_PASSWORD='admin'
    export DJANGO_SUPERUSER_EMAIL="admin@smartdjango.net"
fi
echo "building db..."
python manage.py migrate
python manage.py createsuperuser --noinput
echo "make migrations..."
python manage.py makemigrations SmartDjango
echo "migrate..."
python manage.py migrate SmartDjango
python manage.py collectstatic --noinput
echo [$0] Starting Django Server...
exec gunicorn -w 3 SmartDjango.wsgi:application --bind 0.0.0.0:8080




