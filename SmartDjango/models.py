#  SmartDjango Python Project
#
#  Copyright (c) 2021-25 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

from django.db import models


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    image_path = models.CharField(max_length=30)
    max_speed = models.IntegerField(default=180)

    def __str__(self):
        return self.brand + " " + self.name

