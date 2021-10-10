from django.contrib import admin
from .models import Signup
# Register your models here.
@admin.register(Signup)
class SignUpAdmin(admin.ModelAdmin):
    list_display=["first_name", "last_name","username","password"]
