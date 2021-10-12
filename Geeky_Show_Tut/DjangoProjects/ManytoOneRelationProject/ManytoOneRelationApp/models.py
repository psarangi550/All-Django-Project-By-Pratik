from django.db import models
from django.contrib.auth.models import User# importing the User Model
# Create your models here.
class Post(models.Model):#creating the Model Class Post
    user=models.ForeignKey(User,on_delete=models.SET_DEFAULT,default="1")
    #creating the Foreign to display the fields
    post_cat=models.CharField(max_length=50)
    #defining the CharField For the Same
    post_title=models.CharField(max_length=50)
    #defining the fields for the post model
    post_created_date=models.DateField()
    #defining the Datefield for the model class

    def __str__(self):
        return self.post_title
        #defining the reporesentation of the Model Object
