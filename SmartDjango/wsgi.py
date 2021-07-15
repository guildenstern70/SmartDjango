#  SmartDjango Python Project
#
#  Copyright (c) 2021 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

#
#  SmartDjango Python Project
#
#



import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SmartDjango.settings')

application = Cling(get_wsgi_application())
