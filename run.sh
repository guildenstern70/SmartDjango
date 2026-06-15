#!/bin/bash
#
# SmartDjango Python Project
#
# Copyright (c) 2021-26 Alessio Saltarin
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
echo "using settings: $DJANGO_SETTINGS_MODULE"
python manage.py migrate
python manage.py shell <<'PY'
import os

from django.contrib.auth import get_user_model
from SmartDjango.db_utils import create_users

User = get_user_model()

if User.objects.count() < 3:
    create_users()

username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@smartdjango.net')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
PY
echo "make app migrations..."
python manage.py makemigrations SmartDjango
echo "migrate app..."
python manage.py migrate SmartDjango
python manage.py collectstatic --noinput
python manage.py loaddata initial_data.yaml
echo [$0] Starting Django Server...
exec gunicorn -w 3 SmartDjango.wsgi:application --bind 0.0.0.0:8080



