from django.db import models #importing the models from the django.db models

class StudentManager(models.Manager):#defining the Model Manager
    def get_queryset(self):#defining the get_queryset method which inherit all()
        return super().get_queryset().order_by("name")#returning the queryset object
