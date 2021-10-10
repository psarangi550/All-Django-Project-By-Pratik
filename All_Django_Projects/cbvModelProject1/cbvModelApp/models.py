from django.db import models

# Create your models here.
class Books(models.Model):#creating the Model Class
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    page=models.IntegerField()
    price=models.FloatField()
