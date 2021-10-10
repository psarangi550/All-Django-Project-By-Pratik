from django.db import models

# Create your models here.
class Blog(models.Model):#creating the child class of Model Class
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=500)
