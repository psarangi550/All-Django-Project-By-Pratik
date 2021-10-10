from django.db import models

# Create your models here.
class WFMT_JOBS(models.Model):
    cp_number=models.CharField(max_length=30)
    sne_id=models.IntegerField()
    scheme_number=models.IntegerField()
    trs_area=models.CharField(max_length=6)
    cp_details=models.CharField(max_length=400)

