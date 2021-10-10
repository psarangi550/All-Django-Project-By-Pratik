from django.contrib import admin
from .models import Books #importing the model class in admin.py file
# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):#adm,in class for registering the models
    verbose_name_plural="Book"
    list_display=("title","author","page","price")

