from django.shortcuts import render
class HandlingRequestException(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=self.get_response(request)
        # resp=render(request, "customErrorPageApp/index.html")
        return response
    def process_exception(self,request,exception):
        resp=render(request, "customErrorPageApp/index.html",{"exception":exception.__class__.__name__})
        return resp

