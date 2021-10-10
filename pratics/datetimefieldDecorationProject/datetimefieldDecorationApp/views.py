from django.shortcuts import render
from .forms import AdminForm
# Create your views here.

def index_view(request):
    form=AdminForm()
    return render(request,"datetimefieldDecorationApp/index.html",{"form":form})
