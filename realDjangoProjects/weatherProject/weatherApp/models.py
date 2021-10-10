from django.db import models

# Create your models here.
class Weather(models.Model):#creating the Sub class of Model class
    name=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural="cities"

    def __str__(self):
        return self.name

