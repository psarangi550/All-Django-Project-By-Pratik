from django.db import models
from django.db.models.functions import Lower
from django.db.models import Q
# Create your models here.


# #defining the Manager class for the same as
# class EmployeeManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().order_by(Lower('ename'))
#     def get_emp_range(self,emp1,emp2):
#         return super().get_queryset().filter(esal__range=(emp1,emp2))

# class ProxyEmployeeManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(esal__lt=5000)



class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    esal=models.FloatField()
    eaddress=models.CharField(max_length=200)
    # employees=EmployeeManager()
    # objects=models.Manager()
    class Meta:
        # ordering=("ename",)
        constraints = [
                models.CheckConstraint(check=(Q(esal_lte=2000)),name="esal_constraint"),
                ]



# # class ProxyEmployee(Employee):
# #     objects=ProxyEmployeeManager()
# #     class Meta:
# #         proxy=True
