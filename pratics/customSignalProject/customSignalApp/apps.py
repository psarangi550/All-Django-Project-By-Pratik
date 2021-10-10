from django.apps import AppConfig


class CustomsignalappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customSignalApp'

    def ready(self):
        import customSignalApp.views
