import os, sys, warnings
import kalite

warnings.filterwarnings('ignore', message=r'Module .*? is being added to sys\.path', append=True)

warnings.warn("Using ka-lite.wsgi is deprecated, please use kalite/project/wsgi.py")

PROJECT_PATH = os.path.dirname(os.path.realpath(kalite.__file__))

sys.path = [
    os.path.join(PROJECT_PATH, "packages", "bundled"),
    os.path.join(PROJECT_PATH, "packages", "dist"),
] + sys.path

# After setting up paths, we're ready to proceed with Django config.

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'kalite.project.settings.default'
os.environ['KALITE_HOME'] = '/home/fair/.kalite'
application = WSGIHandler()
