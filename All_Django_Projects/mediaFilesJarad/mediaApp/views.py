from django.shortcuts import render
from mediaApp.models import Employee
# Create your views here.
def img_view(request):
    my_img=Employee.objects.all()
    print(my_img)
    # print(dir(my_img))
    my_dict={"my_img":my_img}
    return render(request,"mediaApp/image.html", context=my_dict)

