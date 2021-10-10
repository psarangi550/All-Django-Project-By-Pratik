from django.apps import AppConfig


class LogincountappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loginCountApp'

    def ready(self):
        import loginCountApp.signals
