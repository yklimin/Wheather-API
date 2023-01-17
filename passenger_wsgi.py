# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1822111/data/www/u1822111.isp.regruhosting.ru/weatherapp')
sys.path.insert(1, '/var/www/u1822111/data/djangoenv1/lib/python3.5/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'weatherapp.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()