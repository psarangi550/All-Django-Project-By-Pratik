from django.apps import AppConfig


class LoginlogoutconfirmappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loginlogoutConfirmApp'

    def ready(self):
        import loginlogoutConfirmApp.signals
