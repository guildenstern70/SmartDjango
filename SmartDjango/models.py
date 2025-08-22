#  SmartDjango Python Project
#
#  Copyright (c) 2021-25 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    name = models.CharField(max_length=30)
    image_path = models.CharField(max_length=30)
    max_speed = models.IntegerField(default=180)

    def __str__(self):
        return f"{self.brand} {self.name}"

