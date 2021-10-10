from django.db import models
# Create your models here.


class Student(models.Model):
    sno=models.AutoField(auto_created=True,primary_key=True)
    sname=models.CharField(max_length=30)
    smark=models.FloatField()
    saddr=models.CharField(max_length=40)

    # def __str__(self):
    #     return self.sname

    # def __str__(self):
    #     return "{}      {}      {}      {}".format(self.sno,self.sname,self.smark,self.saddr)
