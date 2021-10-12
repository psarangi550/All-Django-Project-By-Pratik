from django.db import models

# Create your models here.
class CommonInfo1(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    class Meta:
        abstract = True
#creating another Abstract class which is the child class of the Abstract base class Model
class CommonInfo2(CommonInfo1):
    addr=models.CharField(max_length=100)
    class Meta:
        abstract = True
#creating the sub child class of chil;d class Abstract class to see its behaviour
class Student(CommonInfo2):
    roll=models.IntegerField()
    mark=models.IntegerField()
