#from django.apps import AppConfig
from .apps import AppConfig

class AnalyticsConfig(AppConfig):
    default_auto_field = '.db.models.BigAutoField'
    name = 'analytics'
