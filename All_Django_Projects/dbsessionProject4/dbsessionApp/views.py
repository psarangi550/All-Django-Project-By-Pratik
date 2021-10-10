from django.shortcuts import render,HttpResponse
from .forms import Item
# Create your views here.
def index_view(request):
    form=Item()
    if request.method=="POST":
        form=Item(request.POST)
        if form.is_valid():
            item=form.cleaned_data["item"]
            quantity=form.cleaned_data["quantity"]
            request.session[item]=quantity
            form=Item()
    return render(request, "dbsessionApp/index.html", {"form":form})
def get_view(request):
    return render(request, "dbsessionApp/result.html")
def session_view(request):
    session=request.session
    session.set_expiry(120)
    print(session.get_expiry_date())
    print(session.get_expiry_age())
    return HttpResponse("Hello")
