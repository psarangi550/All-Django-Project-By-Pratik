from django.apps import AppConfig


class RequestresponsesignalappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RequestResponseSignalApp'

    def ready(self):
        import RequestResponseSignalApp.signals
