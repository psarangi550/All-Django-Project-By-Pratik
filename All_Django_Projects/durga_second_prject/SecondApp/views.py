from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time

# Create your views here.
def print_time(request):
    s1 = datetime.datetime.now()
    resp = f""""<h1>Welcome to Django Class </h1>
                    <h2>Corresponding time is {s1.strftime("%A:%B %d:%m:%Y %H:%M:%S %p")}</h2>"""
    return HttpResponse(resp)
