#!/bin/bash
#
# SmartDjango Python Project
#
# Copyright (c) 2021 Alessio Saltarin
# This software is distributed under MIT License.
# See LICENSE.
#
#
echo "make migrations"
python manage.py makemigrations
echo "migrate"
python manage.py migrate
echo [$0] Starting Django Server...
python manage.py runserver


