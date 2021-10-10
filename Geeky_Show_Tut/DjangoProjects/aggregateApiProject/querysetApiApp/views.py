from django.shortcuts import render
from .models import School,Teacher
from .forms import SchoolForm
from django.db.models import Avg,Min,Max,Sum,Count
# Create your views here.
def index_view(request):
    schools=School.objects.all()
    avg=School.objects.all().aggregate(roll_average=Avg("roll"))
    mini=School.objects.all().aggregate(roll_minimum=Min("roll"))
    maxi=School.objects.all().aggregate(roll_maximum=Max("roll"))
    total=School.objects.all().aggregate(roll_sum=Sum("roll"))
    total_count=School.objects.all().aggregate(roll_count=Count("roll"))
    context={"avg":avg,"mini":mini,"maxi":maxi,"total":total,"total_count":total_count,"schools":schools,}
    return render(request,"aggregateApiApp/home.html",context)
