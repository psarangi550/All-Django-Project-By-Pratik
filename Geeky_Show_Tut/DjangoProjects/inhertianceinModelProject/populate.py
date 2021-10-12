import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","inhertianceinModelProject.settings")

import django

django.setup()

import random as random

from inhertianceinModelApp.models import Student

from faker import Faker

fake=Faker("en-IN")

def populate(n):
    for i in range(n):
        name=fake.name()
        email=fake.email()
        addr=fake.address()
        roll=random.randint(00,99)
        mark=fake.random_element([x for x in range (100)])
        Student.objects.get_or_create(name=name,email=email,addr=addr,roll=roll,mark=mark)

populate(20)
