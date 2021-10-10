from django.shortcuts import render

# Create your views here.

def home_view(request,name):
    student={"name":name}
    return render(request, "dynamiccase1App/home.html", context=student)


# #case:-1
# def index_view(request,my_id):
#     student={"my_id": my_id,"name":"Rika"}
#     print(type(student))
#     return render (request,"dynamiccase1App/index.html",student)

#case:-2
# def index_view(request,my_id=1):
#     if my_id==1:
#         student={"my_id":"default","name":"Rika"}
#     if my_id==2:
#         student={"my_id": my_id,"name":"Abismruta"}
#     if my_id==3:
#         student={"my_id": my_id,"name":"Gundu"}
#     return render (request,"dynamiccase1App/index.html",student)

# def sub_index_view(request,my_id,my_sub_id):
#     if my_id==1 and my_sub_id==4:
#         student={"my_id": my_id,"name":"Rika","info":"code_with_pratik"}
#     if my_id==2 and my_sub_id==5:
#         student={"my_id": my_id,"name":"Abismruta","info":"code_with_pratik"}
#     if my_id==3 and my_sub_id==6:
#         student={"my_id": my_id,"name":"Gundu","info":"code_with_pratik"}
#     return render (request,"dynamiccase1App/index.html",student)

