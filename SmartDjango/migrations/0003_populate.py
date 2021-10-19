# Generated by Django 3.2.5 on 2021-09-24 15:17

from django.db import migrations


def create_cars(apps, schema_editor):
    cars_model = apps.get_model('SmartDjango', 'Car')
    car1 = cars_model(
        name="Blu car",
        image_path="/img/269416.png",
        description="A shiny blue car ready to be created or deleted.",
    )
    car2 = cars_model(
        name="Red car",
        image_path="/img/269418.png",
        description="This is a car for passionate men and women.",
    )
    car3 = cars_model(
        name="Green car",
        image_path="/img/269429.png",
        description="A perfect car for the ambientalist fans.",
    )
    car1.save()
    car2.save()
    car3.save()


class Migration(migrations.Migration):

    dependencies = [
        ('SmartDjango', '0002_car'),
    ]

    operations = [
    ]