from django.contrib import admin
from .models import LatLong
# Register your models here.
@admin.register(LatLong)
class LatLongAdmin(admin.ModelAdmin):
    list_display=["zip_code","latitude","longitude"]
