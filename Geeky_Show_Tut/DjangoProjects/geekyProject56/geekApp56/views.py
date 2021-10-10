from django.shortcuts import render
from geekApp56.models import Student
from geekApp56.forms import StudentRegister
# Create your views here.
def index_view(request):#view function with request object 
    if request.method=="POST":
        # stu_obj=Student.objects.get(pk=1169)
        form = StudentRegister(request.POST)#creating the form object with user input
        if form.is_valid():
            # form.save()#saving by using the model form class
            stu_obj=Student(id=1168)#creating a Student Object
            stu_obj.delete()#deleting the student object



            # name=form.cleaned_data["name"]
            # email=form.cleaned_data["email"]
            # password=form.cleaned_data["password"]
            #case:-1:-this is for saving the data using the model class
            # stu=Student( name =name,email=email,password=password)
            # stu.save()
            # #:-case:-2:-this is for updating the data using the model class
            # stu=Student(id=1169, name =name,email=email,password=password)
            # stu.save()

            

            
            
    if request.method == "GET":
        form=StudentRegister()
    return render(request, "geekApp56/index.html", {"form":form})