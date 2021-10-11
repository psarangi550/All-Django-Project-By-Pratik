from django.contrib import admin
from .models import Post,Likes #importing the post model in order to register
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):#defining the model Admin page for the Same
    list_display=["id","user","post_cat","post_name","post_created_date"]

#defining the admin class for the like class which is the subclass of Post class
@admin.register(Likes)
class PostAdmin(admin.ModelAdmin):#defining the model Admin page for the Same
    list_display=["id","post","user","post_cat","post_name","post_created_date"]
