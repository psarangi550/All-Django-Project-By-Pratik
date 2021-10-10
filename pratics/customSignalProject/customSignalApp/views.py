from django.shortcuts import render,HttpResponse
from customSignalApp.signals import notifications
# Create your views here.
def home(request):
    notify=notifications.send_robust(sender=None,request=request,user=["Pratik","Rika"])
    print(notify)
    return HttpResponse("Hello Everyone")
