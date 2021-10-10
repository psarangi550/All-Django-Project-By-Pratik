import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudfbvProject.settings')
import django
django.setup()
from  crudfbvApp.models import Employee
from faker import Faker
import random
fake=Faker("en-IN")
def populate(n):
    for i in range(n):
        eno=random.randint(0000,9999)#generating the random number between 0000-9999
        esal=random.uniform(00000,99999)#generating the float between 00000 to 99999
        ename=fake.name()
        eaddr=fake.address()
        emp=Employee.objects.get_or_create(eno=eno,ename=ename,esal=esal,eaddr=eaddr)
populate(20)

