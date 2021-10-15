import os #importing the Os Model

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ListViewProject.settings")

import django

django.setup()

from ListViewApp.models import Employee

from faker import Faker

import random #importing the random module

fake=Faker("en-IN")


def populate(n):
    for i in range (n):
        eno=random.randint(00,100)
        ename=fake.name()
        esal=random.uniform(0000,9999)
        eaddr=fake.address()
        Employee.objects.get_or_create(eno=eno,ename=ename,esal=esal,eaddr=eaddr)
populate(10)

