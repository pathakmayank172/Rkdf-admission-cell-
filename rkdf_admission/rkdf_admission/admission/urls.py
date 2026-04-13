"""
URL patterns for the Admission app.
Each path() connects a URL to a view function.

Format: path('url/', view_function, name='url_name')
  - 'url/'       : the URL path (what goes in the browser)
  - view_function: the function in views.py to call
  - name=        : a short name to refer to this URL in templates
"""

from django.urls import path
from . import views  # Import all views from this app

urlpatterns = [
    # Home page: http://localhost:8000/
    path('', views.home, name='home'),

    # About page: http://localhost:8000/about/
    path('about/', views.about, name='about'),

    # Courses page: http://localhost:8000/courses/
    path('courses/', views.courses, name='courses'),

    # Admission form: http://localhost:8000/apply/
    path('apply/', views.admission_form, name='admission_form'),

    # Dashboard: http://localhost:8000/dashboard/
    path('dashboard/', views.dashboard, name='dashboard'),

    # Contact page: http://localhost:8000/contact/
    path('contact/', views.contact, name='contact'),
]
