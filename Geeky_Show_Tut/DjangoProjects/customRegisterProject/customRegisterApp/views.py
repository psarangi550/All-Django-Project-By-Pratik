from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.
def index_view(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            form=SignUpForm()
    return render(request, "customRegisterApp/signup.html", {"form":form})
