from django.contrib import admin
from .models import Employee,EmployeeManager,ProxyEmployee
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=["eno","ename","esal","eaddr"]

@admin.register(ProxyEmployee)
class ProxyEmployeeAdmin(admin.ModelAdmin):
    list_display=["eno","ename","esal","eaddr"]

