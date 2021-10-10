from django.db import models

# Create your models here.
class Parent1(models.Model):
    slno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
class Parent2(models.Model):
    address=models.CharField(max_length=100)

class child(Parent1,Parent2):
    residence=models.CharField(max_length=100)

