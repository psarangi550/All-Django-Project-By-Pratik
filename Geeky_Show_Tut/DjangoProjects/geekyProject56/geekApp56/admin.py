from django.contrib import admin
from geekApp56.models import Student #importing the student class from the models module
# Register your models here.
@admin.register(Student)#registering the student into admin.py file
class StudentAdmin(admin.ModelAdmin):#creating the child class of ModelAdmin classes
    list_display=("id","name","email","password")#displaying the list of fiels we want to see in admin console
