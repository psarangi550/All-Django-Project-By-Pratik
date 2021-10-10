from django.apps import AppConfig


class ModelsignalappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modelSignalApp'

    def ready(self):
        import modelSignalApp.signals
