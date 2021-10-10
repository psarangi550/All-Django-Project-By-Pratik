from django.contrib import admin
from .models import Employee #importing the Employee Model Class
# Register your models here.
@admin.register(Employee)
class EmployeeModel(admin.ModelAdmin):
    list_display=["id","eno","ename","esal","eaddr","edate","edatetime"]
