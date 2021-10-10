from django.shortcuts import render
from .models import WFMT_JOBS
from django.http import HttpResponse
# Create your views here.
def index_view(request):
    wfmt_work_list=WFMT_JOBS.objects.all()
    print(type(wfmt_work_list))
    print(wfmt_work_list)
    
    print(dir(wfmt_work_list))
    # print(next(wfmt_work_list))
    my_dict={'wfmt_work_list':wfmt_work_list}
    return render(request,'wfmtApp/index.html',context=my_dict)

def wfmt_view(request):
    return render (request, 'wfmtApp/home.html')

def index1_view(request):
    wfmt_work_list=WFMT_JOBS.objects.all()
    my_type=type(wfmt_work_list)
    print(my_type)
    # my_dict={'wfmt_work_list':wfmt_work_list}
    return HttpResponse(wfmt_work_list)

