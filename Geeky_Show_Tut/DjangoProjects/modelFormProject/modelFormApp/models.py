from django.db import models

# Create your models here.
class StudentTeacherRegistration(models.Model):
    student_name=models.CharField(max_length=100)
    teacher_name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
