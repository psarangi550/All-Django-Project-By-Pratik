from django.db import models

# Create your models here.
class Student(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=100)
    marks=models.IntegerField()
    regi=models.IntegerField(blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=100)
    marks=models.IntegerField()
    regi=models.IntegerField(blank=True)

    def __str__(self):
        return self.name
