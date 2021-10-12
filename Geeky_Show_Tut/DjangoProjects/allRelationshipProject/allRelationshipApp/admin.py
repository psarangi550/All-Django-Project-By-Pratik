from django.contrib import admin
from .models import Song,Page,Post
# Register your models here.

#regisering all model what we have created
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("id","page_cat","page_title","user")
    #defining the requuired fields for the Page Object
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id","post_date","post_name","user")
    #defining the fields  for the Post object which we want to see in the admin console
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("id","song_duration","song_name","sang_by")
    #defining the fields  for the Post object which we want to see in the admin console
