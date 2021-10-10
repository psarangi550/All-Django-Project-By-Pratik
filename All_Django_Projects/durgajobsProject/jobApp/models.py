from django.db import models

# Create your models here.
class Hydjobs(models.Model):
    Date=models.DateTimeField()
    Company = models.CharField(max_length=100)
    Title=models.CharField(max_length=30)
    Eligibility=models.CharField(max_length=10)
    Address=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200)
    Phone_Number=models.IntegerField()
class Bnglrjobs(models.Model):
    Date=models.DateTimeField()
    Company = models.CharField(max_length=100)
    Title=models.CharField(max_length=30)
    Eligibility=models.CharField(max_length=10)
    Address=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200)
    Phone_Number=models.IntegerField()
class Punejobs(models.Model):
    Date=models.DateTimeField()
    Company = models.CharField(max_length=100)
    Title=models.CharField(max_length=30)
    Eligibility=models.CharField(max_length=10)
    Address=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200)
    Phone_Number=models.IntegerField()
class Mumbaijobs(models.Model):
    Date=models.DateTimeField()
    Company = models.CharField(max_length=100)
    Title=models.CharField(max_length=30)
    Eligibility=models.CharField(max_length=10)
    Address=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200)
    Phone_Number=models.IntegerField()

