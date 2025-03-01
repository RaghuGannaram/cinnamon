"""
Healthcheck app configuration.
"""

from django.apps import AppConfig


class HealthcheckConfig(AppConfig):
    """Healthcheck app configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "api.healthcheck"
