from django.db import models

# Create your models here.
#here we are creating the Model classes ot db table field
class Student(models.Model):#creating the child class of Form class which is also a Form class
    name=models.CharField(max_length=30, verbose_name="Enter a Name")
    email=models.EmailField(max_length=50,verbose_name="Enter an Email")
    password=models.CharField(max_length=20)