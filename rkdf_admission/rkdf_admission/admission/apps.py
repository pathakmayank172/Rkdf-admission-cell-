"""
App configuration for the "admission" app.
Django uses this to register and configure the app.
"""

from django.apps import AppConfig


class AdmissionConfig(AppConfig):
    # Default primary key type
    default_auto_field = 'django.db.models.BigAutoField'

    # The name must match the folder name exactly
    name = 'admission'

    # Human-readable name (shown in admin)
    verbose_name = 'Admission Cell'
