from django.apps import AppConfig


class Onetoonerelpart1AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'OnetoOneRelPart1App'

    def ready(self):
        import OnetoOneRelPart1App.signals
