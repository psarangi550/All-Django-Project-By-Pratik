from django.db import models
from django.contrib.auth.models import User #importing the User Model
# Create your models here.

#onetoOne Relationship:-
#-----------------------------
#here we are declaring the onetoone relationship between user and page
#hence an user can create only one page
class Page(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    page_cat=models.CharField(max_length=50)
    page_title=models.CharField(max_length=50)

    def __str__(self):
        return self.page_title

#many to One relationship:-
#---------------------------------
#here between the user and post we are creating the many to one relationship
#hence in here one user can make multiple post but not the otherway around

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_date=models.DateField()
    post_name=models.CharField(max_length=50)

    def __str__(self):#object representation of post
        return self.post_name

#Many to Many Relationship:-
#--------------------------------
#also we are declaring the Many to Many relations between the user and song model
#here one user can sing multiple song and one song can be sang by multiple user

class Song(models.Model):
    user=models.ManyToManyField(User)
    song_name=models.CharField(max_length=50)
    =models.IntegerField()

    #in order to define the manay to many relation ship  we have to display the user info in the song table hence we have to define the fuinction for the same

    def __str__(self):
        return self.song_name

    def sang_by(self):
        return ":".join([ str(u) for u in self.user.all()])
