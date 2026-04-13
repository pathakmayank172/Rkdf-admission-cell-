"""WSGI config for rkdf_admission project."""
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rkdf_admission.settings')
application = get_wsgi_application()
