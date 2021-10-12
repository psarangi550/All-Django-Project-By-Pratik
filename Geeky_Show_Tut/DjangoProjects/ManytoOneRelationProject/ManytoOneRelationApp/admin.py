from django.contrib import admin
from .models import Post #importing models from models.py file
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):#defining the Model Admin class for the same
    list_display=["id","post_cat","post_title","post_created_date","user"]
    #defining all the required field to diplay on the model field
