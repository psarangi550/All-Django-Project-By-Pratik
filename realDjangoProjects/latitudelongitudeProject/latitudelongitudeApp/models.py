from django.db import models

# Create your models here.
class LatLong(models.Model):
    zip_code=models.IntegerField()
    latitude=models.DecimalField(max_digits=9,decimal_places=6,blank=True)
    longitude=models.DecimalField(max_digits=9,decimal_places=6,blank=True)
