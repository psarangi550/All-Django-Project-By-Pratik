from django.contrib import admin
from weatherApp import models
# Register your models here.
@admin.register(models.Weather)
class WeatherAppAdmin(admin.ModelAdmin):
    list_display=["name"]
