"""
WSGI config for fairintranet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

path = os.path.join(
    os.path.split(
        os.path.abspath(
            os.path.dirname(__file__)
        )
    )[:-1]
)[0]
activate_this = os.path.join(path, '../virtualenv/bin/activate_this.py')
if os.path.exists(activate_this):
    execfile(activate_this, dict(__file__=activate_this))
if path not in sys.path:
    sys.path.append(path)
    sys.path.append(path + '/fairintranet')

os.environ["DJANGO_SETTINGS_MODULE"] = "fairintranet.settings.production"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
