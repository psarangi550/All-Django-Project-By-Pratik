from django.contrib import admin
from .models import ToDoList
# Register your models here.
@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display=["id","date","task","task_description"]
