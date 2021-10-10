from django.apps import AppConfig


class DatabasewrappersignalappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'databasewrapperSignalApp'

    def ready(self):
        import databasewrapperSignalApp.signals
