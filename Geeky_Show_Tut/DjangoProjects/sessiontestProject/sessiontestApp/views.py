from django.shortcuts import render

# Create your views here.
def settest(request):
    request.session.set_test_cookie()
    # request.session["name"]="Abismruta"
    return render(request,"sessiontestApp/setsessiontest.html")

def checkcookie(request):
    if request.session.test_cookie_worked():#this is used for testing
        value=request.session.get("name",default=request.session.get_session_cookie_age())
    return render (request, "sessiontestApp/getsessiontest.html",{"value":value})

def deletetest(request):
    request.session.delete_test_cookie()
    return render(request, "sessiontestApp/deletesessiontest.html")
