from django.contrib import admin
from chucknorrisApp import models
# Register your models here.
# class Chuck_Choice_Admin(admin.ModelAdmin):
#     list_display=["roles"]

admin.site.register(models.Chuck_Choice)

