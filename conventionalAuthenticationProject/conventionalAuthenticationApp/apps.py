from django.apps import AppConfig


class ConventionalauthenticationappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'conventionalAuthenticationApp'
    def ready(self):
        import conventionalAuthenticationApp.signals
