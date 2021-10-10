def HelloMiddlware(get_response):
    def PrintHello(request):
        print("hello") #printing Hello to the server console before the request hit the view function
        response=get_response(request)#forwarding the request to the next Middleware/view function
        return response #returning the response which we got from the view function
    return PrintHello #returning the PrintHello function which internally represent the __call__(self,request)
