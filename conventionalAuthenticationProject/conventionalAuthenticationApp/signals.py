from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User

#here we are defining the receiver function

@receiver(signal=user_logged_in,sender=User)
def ip_rendering_at_login(sender,request,user,**kwargs):
    server_port=request.META.get("SERVER_PORT")
    ip_address=request.META.get("REMOTE_ADDR")
    request.session["ip"]=ip_address
    request.session["port"]=server_port



