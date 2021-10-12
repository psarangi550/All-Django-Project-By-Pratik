from django.apps import AppConfig


class LatitudelongitudeappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'latitudelongitudeApp'

    def ready(self):
        import latitudelongitudeApp.signals#importing the signals module
