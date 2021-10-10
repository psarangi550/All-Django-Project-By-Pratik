from django.shortcuts import render

# Create your views here.
#setting the session
def setsession(request):
    request.session["name"]="Abismruta"
    return render(request, "sessionBasicApp/setsession.html",)

#getting the session data from the django_session table
def getsession(request):
    name=request.session.get("name","Guest")
    return render (request,"sessionBasicApp/getsession.html", {"name":name})


#to delete a session we have to uise this function
def deletesession(request):
    request.session.flush()
    return render(request,"sessionBasicApp/deletesession.html")
