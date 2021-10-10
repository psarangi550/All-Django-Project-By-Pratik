from django.shortcuts import render
from Django_Durga.All_Django_Projects.templateProject.templates import tempApp
import datetime
# Create your views here.
def my_temp_view(request):
    dt=datetime.datetime.now()
    my_dict={"time":dt.strftime("%A:%B %d:%m:%Y %H:%M:%S %p")}
    return render(request,"tempApp/index.html",context=my_dict)