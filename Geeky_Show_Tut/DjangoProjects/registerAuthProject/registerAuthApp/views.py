from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm #importing the UserCtreationForm Model form from auth module forms
# Create your views here.
def index_view(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form=UserCreationForm()
    return render(request, "registerAuthApp/signup.html", {"form":form})
