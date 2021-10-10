from django.shortcuts import render
from .models import School,Teacher
from .forms import SchoolForm
from django.db.models import Avg,Min,Max
# Create your views here.
def index_view(request):
   # school=School.objects.get(id=1)
   # school=School.objects.order_by("name").first()
   # school=School.objects.order_by("name").last()
   # school=School.objects.latest("roll")
   # school=School.objects.earliest("roll")
   #case:-1:-exist()
   #-----------
   # school=School.objects.filter(id=55).exists()
   # print(school)
   # sch=School.objects.get(marks=72)
   # school=School.objects.filter(marks=sch.marks).exists()
   # print(school)
   #case:-2:-create():-on queryset object only
   # #--------------------
   # school=School.objects.create(name="Abismruta",roll=56,city="Banagalore",marks=78,pass_date="2021-10-09")
   # print(school)
   #case:-3:-bulk_create():-
   #--------------------------
   # sch1=School(name="Rika",roll=100,city="Banagalore",marks=98,pass_date="2021-09-09")
   # sch2=School(name="Abi",roll=101,city="Banagalore",marks=88,pass_date="2021-08-09")
   # sch3=School(name="Gundu",roll=102,city="Banagalore",marks=58,pass_date="2021-11-09")
   # school=School.objects.bulk_create([sch1,sch2,sch3])
   # print(school)
   #case:-4:-get_or_create():-
   #---------------------------
   # school,created=School.objects.get_or_create(name="Rika",roll=100,city="Banagalore",marks=98,pass_date="2021-09-09")
   # print(created)
   # school,created=School.objects.get_or_create(name="Shalini",roll=103,city="Banagalore",marks=98,pass_date="2021-09-09")
   # print(created)
   #case:-5:-update():-always on queryset objects
   #----------------------
   # school=School.objects.filter(marks=72).update(name="Pratik")
   # print(school)
   #case:-6:-bulk_update(default={},fields=[])
   #------------------------------------------
   # sch1=School(name="Papali",roll=104,city="Banagalore",marks=99,pass_date="2021-09-09")
   # sch2=School(name="Pupuli",roll=105,city="Banagalore",marks=98,pass_date="2021-08-09")
   # sch3=School(name="Puja",roll=106,city="Banagalore",marks=57,pass_date="2021-11-09")
   # School.objects.bulk_create([sch1,sch2,sch3])
   # sch1=School.objects.get(roll=104)
   # sch2=School.objects.get(roll=105)
   # sch3=School.objects.get(roll=106)
   # sch1.city="Odisha"
   # sch2.city="New York"
   # sch3.city="Hyderbad"
   # school=School.objects.bulk_update([sch1,sch2,sch3],["city"])
   #ex:-2:-bulk_update() on queryset object:-TRICKY BUT UNDERSTANDABLE
   #------------------------------------------
   # school=School.objects.all()
   # for sch in school:
   #  sch.marks=60
   #  School.objects.bulk_update(school,["marks"])
   # print(school)
   #CASE:-7:-update_or_create():-
   #----------------------------------------
   # school,created=School.objects.update_or_create(defaults={"marks":78}, id=5)
   # print(school)
   # print(created)
   #case:-8:-in_bulk(id=[],field_name="pk")
   #--------------------------------------------
   # school=School.objects.in_bulk()
   # print(school)
   # school=School.objects.in_bulk([])
   # print(school)
   # school=School.objects.in_bulk([7,8])
   # print(school)
   # print(school[7].name)
   # print(school[8].name)
   #CASE:-9:-check():-already knew ,aggregate():-already knew,delete():-knew
   #-----------------------------------------------------------
   school=School.objects.all().explain()#:-explain() to explain the query
   print(school)
   return render(request,"querysetApiApp/home.html",{"school":school})
