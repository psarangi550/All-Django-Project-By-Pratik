from django.db.models.signals import pre_save #importing the pre_save signal
from .models import LatLong #importing the own Model class
from django.dispatch import receiver
import requests #importing the request module
@receiver(signal=pre_save,sender=LatLong)
def before_save(sender,instance,**kwargs):
    print("signal working")
    zip=instance.zip_code
    resp=requests.get(f"https://documentation-resources.opendatasoft.com/api/records/1.0/search/?dataset=doc-geonames-cities-5000&q={zip}&facet=country_code&facet=population")
    instance.latitude=resp.json()["records"][0]["geometry"]["coordinates"][0]
    instance.longitude=resp.json()["records"][0]["geometry"]["coordinates"][1]
