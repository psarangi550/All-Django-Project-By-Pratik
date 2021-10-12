from django.shortcuts import render,HttpResponseRedirect
from .forms import LatLongForm
from .models import LatLong
# Create your views here.
def index_view(request):
    form=LatLongForm()
    if request.method=="POST":
        form=LatLongForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/display/")
    return render(request, "latitudelongitudeApp/index.html", {"form":form})
def display_view(request):
    latlong=LatLong.objects.all()
    return render(request,"latitudelongitudeApp/display.html",{"latlong":latlong})
