import os #importing the os module
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","durgajobsProject.settings")
django.setup()

from jobApp.models import *
import faker
import random
import datetime
fake=faker.Faker("en-IN")
def prepare(n):
    for i in range(n):
        fd=datetime.datetime.strptime(fake.date(),"%Y-%m-%d")
        fdate=fd
        fcomapany=fake.random_element(elements=("TCS","WIPRO","TECH_MAHINDRA","INFOSYS","CEE BEE"))
        ftittle=fake.random_element(elements=("SOFTWARE ENGG","MANAGER","TEAM LEAD","TEST LEAD"))
        felg=fake.random_element(elements=("BTECH","MTECH","MCA","INTERIOR"))
        faddr=fake.address()
        femail=fake.email()
        fphone=int(fake.phone_number()[1:])
        Hydjobs.objects.get_or_create(Date=fdate,Company=fcomapany,Title=fcomapany,Eligibility=felg,Address=faddr,Email=femail,Phone_Number=fphone)
        Bnglrjobs.objects.get_or_create(Date=fdate,Company=fcomapany,Title=fcomapany,Eligibility=felg,Address=faddr,Email=femail,Phone_Number=fphone)
        Punejobs.objects.get_or_create(Date=fdate,Company=fcomapany,Title=fcomapany,Eligibility=felg,Address=faddr,Email=femail,Phone_Number=fphone)
        Mumbaijobs.objects.get_or_create(Date=fdate,Company=fcomapany,Title=fcomapany,Eligibility=felg,Address=faddr,Email=femail,Phone_Number=fphone)
prepare(25)

