# Generated by Django 3.2.5 on 2021-07-16 08:44
from django.contrib.auth.hashers import make_password
from django.db import migrations


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


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_users)
    ]