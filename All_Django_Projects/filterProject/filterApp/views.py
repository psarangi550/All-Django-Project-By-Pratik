from django.shortcuts import render
from .models import FilterModel
# Create your views here.
def index_view(request):
    data_list=FilterModel.objects.all()
    my_dict={"data_list":data_list}
    return render(request, "filterApp/index.html", context=my_dict)
