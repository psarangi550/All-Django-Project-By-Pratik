from django.db import models
from django.urls import reverse
# Create your models here.
class Beer(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    taste=models.CharField(max_length=100)
    percentage_of_alchol=models.DecimalField(max_digits=4,decimal_places=2)
    choice=[("inida","INDIA"),("united Kingdom","UK"),("states","USA")]
    manufacture=models.CharField(choices=choice,max_length=20,default=False)
    is_alcholic=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("detail",kwargs={"pk":self.id})
