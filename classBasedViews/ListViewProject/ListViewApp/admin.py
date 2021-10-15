from django.contrib import admin
from .models import Employee #importing the Employee class
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=["id","eno","ename","esal","eaddr"]

