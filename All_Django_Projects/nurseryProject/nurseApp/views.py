from django.shortcuts import render
import datetime#importing the datetime module
# Create your views here.
def temp_view(request):
    dt=datetime.datetime.now()
    name="Abismruta"
    msg=""
    if dt.hour<12:
        msg="Good Morning"
    elif dt.hour<16:
        msg="Good Afternoon"
    elif dt.hour<21:
        msg="Good Evening"
    else:
        msg="Good Night"
    my_dict={"name":name,"msg":msg,"date":dt}
    return render(request, "nurseApp/index.html",context=my_dict)


