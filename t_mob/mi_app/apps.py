# mi_app/apps.py
from django.apps import AppConfig

class MiAppConfig(AppConfig):
    name = 'mi_app'

    def ready(self):
        import mi_app.signals