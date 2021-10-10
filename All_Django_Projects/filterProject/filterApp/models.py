from django.db import models

# Create your models here.
class FilterModel(models.Model):
    org_name=models.CharField(max_length=100)
    course_name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    date=models.DateField()

