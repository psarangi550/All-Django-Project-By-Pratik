from django.contrib import admin
from .models import StudentTeacherRegistration
# Register your models here.
@admin.register(StudentTeacherRegistration)
class StudentTeacherRegistrationAdmin(admin.ModelAdmin):
    list_display=[ "student_name", "teacher_name","email","password"]
