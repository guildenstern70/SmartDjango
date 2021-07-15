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

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SmartDjango.settings')

application = get_asgi_application()
