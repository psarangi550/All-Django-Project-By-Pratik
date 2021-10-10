from django.apps import AppConfig


class BuiltinsignalappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'builtinSignalApp'

    def ready(self):
        import builtinSignalApp.signals
