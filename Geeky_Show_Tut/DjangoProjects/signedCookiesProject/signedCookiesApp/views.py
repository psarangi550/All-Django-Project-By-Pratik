from django.shortcuts import render

# Create your views here.
def setsignedcookies(request):
    resp=render(request,"signedCookiesApp/setcookies.html")
    resp.set_signed_cookie("name","Abismruta",salt="prove")
    return resp #returning the response

#to get the Cookies that set by server
def getcookie(request):
    name=request.get_signed_cookie(key="name",default="Guest", salt="prov")
    return render(request,"signedCookiesApp/getcookies.html",{"name":name})

