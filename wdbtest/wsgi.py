"""
WSGI config for wdbtest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wdbtest.settings')

application = get_wsgi_application()

from wdb.ext import WdbMiddleware
application = WdbMiddleware(application)
