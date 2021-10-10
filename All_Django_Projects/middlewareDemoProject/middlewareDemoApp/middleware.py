from django.shortcuts import render
class ExecutionMiddleware(object):
    def __init__(self, get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("This is the Response from 1st Middleware")
        response=self.get_response(request)
        return response
class NextExectution(object):
    def __init__(self, get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("This is the Response from 2nd Middleware")
        response=self.get_response(request)
        print("This is the Response from 2nd Middleware")
        return response


