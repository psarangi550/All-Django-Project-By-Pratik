from django.db import models

# Create your models here.
class StudentFeedback(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    marks=models.CharField(max_length=200)
    feedback=models.CharField(max_length=200)
