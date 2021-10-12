from django.contrib import admin
from .models import Student,CommonInfo1,CommonInfo2
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=["roll","mark"]

# @admin.register(CommonInfo2)
# class CommonInfo2Admin(admin.ModelAdmin):
#     list_display=["id","name","email","address"]

# @admin.register(CommonInfo1)
# class CommonInfo1Admin(admin.ModelAdmin):
#     list_display=["id","name","email"]
