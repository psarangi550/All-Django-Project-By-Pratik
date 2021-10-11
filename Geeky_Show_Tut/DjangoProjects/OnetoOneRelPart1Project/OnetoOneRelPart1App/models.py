from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):#creating the model class linking the auth User Model as one to one relationship
    user=models.OneToOneField(to=User,on_delete=models.CASCADE)
    #here if we are deleting the user then Post will be deleted Automatically
    post_cat=models.CharField(max_length=50,)
    post_name=models.CharField(max_length=50,)
    post_created_date=models.DateField()

    def __str__(self):#defing the object representation
        return self.user.username
    #defining the fields for the 2nd Model i.e the User Model
class Likes(Post):
    post=models.OneToOneField(to=Post,on_delete=models.CASCADE, parent_link=True)
    like=models.IntegerField()

    def __str__(self):#defing the object representation
        return self.post.user.username
