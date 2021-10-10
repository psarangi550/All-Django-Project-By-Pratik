from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed #these are the builtin signal
from django.contrib.auth.models import User #importing User Model for the Signal
from django.dispatch import receiver #importing the receiver decorator

#now here we are defining the receiver function

#this receiver function will act when the user logged in by login(request,user)
@receiver(user_logged_in,sender=User)
def when_user_login(sender,**kwargs):
    print("sender", sender)
    # print("Request", request)
    # print("User", user)
    # print("Username", user.username)
    # print("Password", user.password)
    print("Additional Args", kwargs)


#This receiver function will work or act when the logout(request) will run
@receiver(user_logged_out,sender=User)
def when_user_logout(sender,request,user,**kwargs):
    print("------------------------------------")
    print("User Logout Activity")
    print("sender", sender)
    print("Request", request)
    print("User", user)
    print("Username", user.username)
    print("Password", user.password)
    print("Additional Args", kwargs)

#this function will work on when the user _login_failed
@receiver(signal=user_login_failed,sender=None)
def when_user_login_failed(sender,request,credentials,**kwargs):
    print("******************************************")
    print("This will run when the User Login Failed")
    print(f"sender:-{sender}")
    print(f"credetional:-{credentials}")
    print(f"Request:-{request}")
    print(f"Additional Argument:-{kwargs}")
