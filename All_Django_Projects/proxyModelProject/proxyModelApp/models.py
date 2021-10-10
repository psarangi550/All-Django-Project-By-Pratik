from django.db import models

# Create your models here.

class EmployeeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("esal")[:20]

class ProxyEmployeeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("eno")[:10]


class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    esal=models.IntegerField()
    eaddr=models.CharField(max_length=100)
    objects=models.Manager()
    custom=EmployeeManager()

class ProxyEmployee(Employee):
    objects=ProxyEmployeeManager()
    class Meta:
        ordering=("ename",)
        proxy=True
