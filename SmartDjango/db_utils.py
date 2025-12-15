#  SmartDjango Python Project
#
#  Copyright (c) 2021-25 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

from django.contrib.auth.hashers import make_password

def create_users(apps, schema_editor):
    user_model = apps.get_registered_model('auth', 'User')
    user1 = user_model(
        username='axsaxs',
        email='alessiosaltarin@gmail.com',
        password=make_password('lzdwzo'),
        is_superuser=False,
        is_staff=True
    )
    user2 = user_model(
        username='guest',
        email='guest@smartdjango.net',
        password=make_password('guest'),
        is_superuser=False,
        is_staff=False
    )
    user1.save()
    user2.save()
