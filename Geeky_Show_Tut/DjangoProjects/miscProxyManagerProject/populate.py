import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","miscProxyManagerProject.settings")

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
        roll=random.randint(00,99)
        mark=fake.random_element([x for x in range (100)])
        Student.objects.get_or_create(name=name,email=email,roll=roll,mark=mark)

populate(5)
