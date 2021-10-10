from django.contrib import admin
from .models import Beer
# Register your models here.
@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    list_display = ("name","price","taste","percentage_of_alchol","manufacture","is_alcholic")
