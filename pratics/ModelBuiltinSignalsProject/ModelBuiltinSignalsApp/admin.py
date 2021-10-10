from django.contrib import admin
from .models import Student,Employee
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=["roll","name","marks","regi"]

@admin.register(Employee)
class StudentAdmin(admin.ModelAdmin):
    list_display=["roll","name","marks","regi"]
