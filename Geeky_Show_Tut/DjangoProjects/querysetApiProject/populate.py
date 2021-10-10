import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","querysetApiProject.settings")

import django

django.setup()

from faker import Faker

import random

from querysetApiApp.models import School,Teacher

fake=Faker("en-IN")

def populate(n):
    for i in range(n):
        name=fake.name()
        empno=random.randint(00,99)
        salary=random.randint(00000,99999)
        city=fake.city()
        pass_date=fake.date()
        Teacher.objects.get_or_create(name=name,empno=empno,salary=salary,city=city,pass_date=pass_date)

populate(2)
