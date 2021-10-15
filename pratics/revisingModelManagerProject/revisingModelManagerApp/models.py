from django.db import models

# Create your models here.
class CustomManager(models.Manager):
    def get_query_set(self):
        return super().get_query_set().order_by("-ename")
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=100)
    custom=CustomManager()
    objects=models.Manager()
