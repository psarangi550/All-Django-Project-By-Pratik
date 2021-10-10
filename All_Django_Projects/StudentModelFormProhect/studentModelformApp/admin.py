from django.contrib import admin
from .models import Student #importing the student class from the models module
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=["name","email","password","cpassword"]
admin.site.register(Student, StudentAdmin)
