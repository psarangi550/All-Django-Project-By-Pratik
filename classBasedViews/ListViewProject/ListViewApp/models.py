from django.db import models

# Create your models here.
class Employee(models.Model):#defining the Model Class
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=100)

