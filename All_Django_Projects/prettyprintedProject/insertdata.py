import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","prettyprintedProject.settings")
django.setup()

from django import db
db.connection.cursor().close()

from prettyApp.models import Student
new_student=Student.objects.get_or_create(sname="Rohit")