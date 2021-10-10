from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import logout,login
# Create your views here.
import pyrebase
config = {
  "apiKey": "AIzaSyANWyUCnnuvxeMQuWAW49vPHWPPrptNU3E",
  "authDomain": "pratikproject-327318.firebaseapp.com",
  "databaseURL": "https://pratikproject-327318-default-rtdb.firebaseio.com",
  "projectId": "pratikproject-327318",
  "storageBucket": "pratikproject-327318.appspot.com",
  "messagingSenderId": "693441829812",
  "appId": "1:693441829812:web:38967362710e450e7430e1",
  "measurementId": "G-9H37E5QY8E"
};
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def login_view(request):
    if request.method == "POST":
        email=request.POST.get('email')
        passw=request.POST.get("pass")
        user = auth.sign_in_with_email_and_password(email, passw)
        request.session["user"]=user
        return HttpResponseRedirect("/index/")
    return render (request , "integratingFirBaseDjangoApp/login.html")

def index_view(request):
    data=request.session.get("user")["email"]
    return HttpResponse(f"Welcome {data}")
