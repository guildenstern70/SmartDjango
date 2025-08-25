#  SmartDjango Python Project
#
#  Copyright (c) 2021-25 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

from django.test import TestCase

from SmartDjango.urls import urlpatterns


class SmartDjangoTests(TestCase):

    def test_home_page_existance(self):
        home = urlpatterns[1]
        self.assertEqual(home.name, 'home')


