from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.AutoField(auto_created=True,primary_key=True)
    ename=models.CharField(max_length=100)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=100)
