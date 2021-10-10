from django.shortcuts import render
from .models import School,Teacher
from .forms import SchoolForm
# Create your views here.
def index_view(request):
    # form=SchoolForm()
    # qs1=School.objects.values_list("id","name",named=True)
    # qs2=Teacher.objects.values_list("id","name",named=True)
    # schools=qs1.difference(qs2)
    # print("*********************")
    # print(schools.query)
    # print("*********************")
    # schools=School.objects.order_by("?")
    schools=School.objects.values("pass_date").dates("pass_date","year","ASC",)

    print("*********************")
    print(schools)
    print("*********************")
    print(schools.query)
    print("*********************")

    return render(request,"querysetApiApp/home.html",{"schools":schools})
