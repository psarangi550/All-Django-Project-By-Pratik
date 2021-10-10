from django.contrib import admin
from .models import Movie
# # Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display=["id","relese_date","movie_name","hero","heroine","director","rating"]

# admin.site.register(Movie,MovieAdmin)
