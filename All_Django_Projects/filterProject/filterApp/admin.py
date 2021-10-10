from django.contrib import admin
from .models import  FilterModel
# Register your models here.
@admin.register(FilterModel)
class FilterModelAdmin(admin.ModelAdmin):
    list_display=["org_name","course_name","category","date"]
