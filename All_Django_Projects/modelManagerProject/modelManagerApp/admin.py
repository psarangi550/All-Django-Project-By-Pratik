from django.contrib import admin
from .models import  Employee
# Register your models here.
# @admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=["eno",'ename','esal','eaddress']

# class ProxyEmployeeAdmin(admin.ModelAdmin):
#     list_display=["eno",'ename','esal','eaddress']

admin.site.register(Employee,EmployeeAdmin)
# admin.site.register(ProxyEmployee,ProxyEmployeeAdmin)
