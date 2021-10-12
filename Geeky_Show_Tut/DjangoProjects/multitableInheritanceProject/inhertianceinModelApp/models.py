from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
#creating the sub child class of child class  Parent class to see its behaviour
class Student(CommonInfo):
    roll=models.IntegerField()
    mark=models.IntegerField()
