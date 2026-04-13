"""
Django settings for RKDF University Admission Cell Website
This file contains all the configuration for the Django project.
"""

import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for Django (keep this secret in production!)
SECRET_KEY = 'django-insecure-rkdf-university-ranchi-admission-cell-2024'

# Debug mode: Set to False in production
DEBUG = True

# Hosts allowed to access this site
ALLOWED_HOSTS = ['*']

# -------------------------------------------------------
# Installed Applications
# Django built-in apps + our custom "admission" app
# -------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',        # Admin panel
    'django.contrib.auth',         # Authentication
    'django.contrib.contenttypes', # Content types framework
    'django.contrib.sessions',     # Session management
    'django.contrib.messages',     # Flash messages
    'django.contrib.staticfiles',  # Static files management
    'admission',                   # Our custom admission app
]

# Middleware: processes requests and responses
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration file
ROOT_URLCONF = 'rkdf_admission.urls'

# Template configuration: tells Django where to find HTML files
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # We use app-level templates
        'APP_DIRS': True,  # Django will look in each app's "templates" folder
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rkdf_admission.wsgi.application'

# -------------------------------------------------------
# Database Configuration
# Using SQLite (default, no extra setup needed)
# -------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Database file in project root
    }
}

# Password validation rules
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'  # Indian Standard Time
USE_I18N = True
USE_TZ = True

# -------------------------------------------------------
# Static Files (CSS, JavaScript, Images)
# -------------------------------------------------------
STATIC_URL = '/static/'  # URL prefix for static files
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Where collectstatic puts files

# Primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
