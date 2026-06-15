#  SmartDjango Python Project
#
#  Copyright (c) 2021-26 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


def create_users(apps=None, schema_editor=None):
    user_model = apps.get_model('auth', 'User') if apps else get_user_model()
    user_model.objects.get_or_create(
        username='axsaxs',
        defaults={
            'email': 'alessiosaltarin@gmail.com',
            'password': make_password('lzdwzo'),
            'is_superuser': False,
            'is_staff': True,
        },
    )
    user_model.objects.get_or_create(
        username='guest',
        defaults={
            'email': 'guest@smartdjango.net',
            'password': make_password('guest'),
            'is_superuser': False,
            'is_staff': False,
        },
    )
