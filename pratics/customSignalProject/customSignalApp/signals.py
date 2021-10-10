from django.dispatch import Signal,receiver

notifications=Signal(providing_args=["request","user"])

#creating a signal object by providing args as argument

@receiver(signal=notifications)
def my_notification(sender,request,user,**kwargs):
    print(f"sender-->{sender}")
    print(f"Request-->{request}")
    print(f"User-->{user}")
    print(f"Arguments-->{kwargs}")
