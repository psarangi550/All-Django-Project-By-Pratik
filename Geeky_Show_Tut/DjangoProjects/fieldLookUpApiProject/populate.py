import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","fieldLookUpApiProject.settings")

import django

django.setup()

from faker import Faker

from fieldLookUpApiApp.models import Employee

import random

fake=Faker("en-IN")

def populate(n):
    for i in range(n):
        eno=random.randint(00,99)
        ename=fake.name()
        esal=random.randint(0000,9999)
        eaddr=fake.address()
        edate=fake.date()
        edatetime=fake.date_time()
        Employee.objects.get_or_create(eno=eno,ename=ename,esal=esal,eaddr=eaddr,edate=edate,edatetime=edatetime)

populate(2)


