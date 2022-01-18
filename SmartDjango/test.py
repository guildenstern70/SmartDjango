#  SmartDjango Python Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

#  SmartDjango Python Project
#
#

from django.test import TestCase
from SmartDjango.urls import urlpatterns


class SmartDjangoTests(TestCase):

    def test_home_page_existance(self):
        home = urlpatterns[1]
        self.assertEqual(home.name, 'home')


