from django.contrib import admin
from .models import Student
# Register your models here.
admin.site.site_header="Pratik's Dashboard"
admin.site.site_title="My Employee List"
admin.site.index_title="My Employee List"
class myadmin(admin.ModelAdmin):
    # list_display=['sno','sname','smark','saddr']
    list_filter=['sno','sname']




admin.site.register(Student,myadmin)
