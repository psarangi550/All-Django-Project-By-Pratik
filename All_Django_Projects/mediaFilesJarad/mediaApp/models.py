from django.db import models

# Create your models here.
class Employee(models.Model):
    photo=models.ImageField()

    class Meta:
        verbose_name_plural="Pratik _Employee"

    def __str__(self):
        return self.photo.path