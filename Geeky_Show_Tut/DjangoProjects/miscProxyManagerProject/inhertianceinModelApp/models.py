from django.db import models
from .manager import StudentManager
# Create your models here.
class CommonInfo(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    class Meta:
        abstract = True
#creating the sub child class of child class  Parent class to see its behaviour
class Student(CommonInfo):
    roll=models.IntegerField()
    mark=models.IntegerField()
    objects=models.Manager()

#defining the Proxy model
class ProxyStudent(Student):
    custom=StudentManager()
    class Meta:
        proxy=True




