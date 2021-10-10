from django.apps import AppConfig


class ModelbuiltinsignalsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ModelBuiltinSignalsApp'

    def ready(self):
        import ModelBuiltinSignalsApp.signals
