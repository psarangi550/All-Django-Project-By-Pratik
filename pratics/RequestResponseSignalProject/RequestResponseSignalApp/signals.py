from django.core.signals import request_started,request_finished, got_request_exception
from django.dispatch import receiver


#defining the receiver function over here

# @receiver(signal=request_started)
# def request_begin_signal(sender,**kwargs):
#     print("==============================")
#     print(f"Request Started")
#     print(f"Sender:-{sender}")
#     print(f"Arguments:-{kwargs}")
#     print("==============================")

# @receiver(signal=request_started)
# def request_begin_signal(sender,**kwargs):
#     print("++++++++++++++++++++++++++++++++")
#     print(f"Request Started")
#     print(f"Sender:-{sender}")
#     print(f"Arguments:-{kwargs}")
#     print("+++++++++++++++++++++++++++++++++")

@receiver(signal=got_request_exception)
def request_begin_signal(sender,request,**kwargs):
    print("++++++++++++++++++++++++++++++++")
    print(f"Request Started")
    print(f"Sender:-{sender}")
    print(f"Request:-{request}")
    print(f"Arguments:-{kwargs}")
    print("+++++++++++++++++++++++++++++++++")


