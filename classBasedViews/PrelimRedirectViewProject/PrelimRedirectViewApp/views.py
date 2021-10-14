from django.shortcuts import render
from django.views.generic.base import RedirectView,TemplateView,View
# Create your views here.
# class MyRedirectView(RedirectView):
#     url="/"
#     permanent=True
#     query_string=True

#     def get_redirect_url(self,*args,**kwargs):
#         print(kwargs)
#         return super().get_redirect_url(*args,**kwargs)

class MyView(View):
    template_name=""
    def get(self,request):
        # name=request.GET.get("name")
        # print(name)
        print(request.GET)
        return render(request, self.template_name)


class MyRedirectView(RedirectView):
    query_string=False
    url="/"
    permant=True
    template_name=""

    def get_redirect_url(self,*args,**kwargs):
        print(kwargs)
        print(args)
        return super().get_redirect_url(*args,**kwargs)
    # def get(self,request,id):
    #     print(request.GET)
    #     return render(request, self.template_name)
