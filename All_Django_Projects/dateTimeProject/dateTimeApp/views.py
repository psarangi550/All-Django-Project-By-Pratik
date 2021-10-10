from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def welcome(request):
    msg="<h1>Hello Guest"
    dt=datetime.datetime.now()
    if dt.hour <12:
        msg=msg+"Good Morning</h1>"
    elif dt.hour <16:
        msg=msg+"Good Morning</h1>"
    elif dt.hour <21:
        msg=msg+"Good Morning</h1>"
    else:
        msg=msg+"Good Morning</h1>"
    msg=msg+"<h1> Now the Server time is:"
    msg+=dt.strftime("%A:%B %d:%m:%Y %H:%M:%S %p")
    return HttpResponse(msg)

