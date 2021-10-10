from django.db import models
from django.db.models import Q

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=100)
    class Meta:
        constraints=[
            models.CheckConstraint(check=Q(ename__gte="Abi"),name="Name Must Be Abi")
        ]

    def __str__(self):
        return self.ename
