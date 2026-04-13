"""
Main URL Configuration for RKDF University Admission Cell
This file routes URLs to the correct app.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin Panel - accessible at /admin/
    path('admin/', admin.site.urls),

    # All other URLs are handled by the "admission" app
    # The empty string '' means these URLs start from the root
    path('', include('admission.urls')),
]
