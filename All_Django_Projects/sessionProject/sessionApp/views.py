from django.shortcuts import render,HttpResponse

# Create your views here
#remember to migrate the table otherwise it will not work.
def index_view(request):
    # return HttpResponse("Hello")
    count=request.session.get("count",0)#fetching the session from the user
    new_count=count+1 #here  we adding the new count value
    request.session["count"]=new_count #here adding the client info to the session data
    request.session.set_expiry(180)
    print(request.session.get_expiry_date())
    print(request.session.get_expiry_age())
    return render (request, "sessionApp/index.html", {"my_count":new_count})
    #sending the new count value to the templates page
