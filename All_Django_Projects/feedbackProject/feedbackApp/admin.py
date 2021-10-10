from django.contrib import admin
from . import models
# Register your models here.
class StudentFeedbackAdmin(admin.ModelAdmin):
    list_display=["name","email","marks","feedback"]
admin.site.register(models.StudentFeedback,StudentFeedbackAdmin)
