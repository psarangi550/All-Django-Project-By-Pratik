from django.db import models

# Create your models here.
class ToDoList(models.Model):
    date=models.DateField()
    task=models.CharField(max_length=100)
    task_description=models.TextField()

