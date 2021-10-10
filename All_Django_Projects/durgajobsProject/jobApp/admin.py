from django.contrib import admin
from .models import Hydjobs,Bnglrjobs,Punejobs,Mumbaijobs
# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display=["Date","Company","Title","Eligibility","Address","Email","Phone_Number"]
class BnglrjobsAdmin(admin.ModelAdmin):
    list_display=["Date","Company","Title","Eligibility","Address","Email","Phone_Number"]
class PunejobsAdmin(admin.ModelAdmin):
    list_display=["Date","Company","Title","Eligibility","Address","Email","Phone_Number"]
class MumbaijobsAdmin(admin.ModelAdmin):
    list_display=["Date","Company","Title","Eligibility","Address","Email","Phone_Number"]

admin.site.register(Hydjobs,HydjobsAdmin)
admin.site.register(Bnglrjobs,BnglrjobsAdmin)
admin.site.register(Punejobs,PunejobsAdmin)
admin.site.register(Mumbaijobs,MumbaijobsAdmin)
