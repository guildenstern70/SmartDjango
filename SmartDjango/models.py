#  SmartDjango Python Project
#
#  Copyright (c) 2021-23 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
from django.db import models


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    image_path = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

