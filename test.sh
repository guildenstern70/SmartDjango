#!/bin/bash
#
# SmartDjango Python Project
#
# Copyright (c) 2021-25 Alessio Saltarin
# This software is distributed under MIT License.
# See LICENSE.
#
#
export DJANGO_SETTINGS_MODULE=SmartDjango.settings
echo "tests"
python manage.py test
