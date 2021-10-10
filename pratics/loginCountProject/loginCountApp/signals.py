from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.shortcuts import HttpResponseRedirect,render
from django.core.cache import cache

@receiver(user_logged_in,sender=User)
def login_count_signal(sender,request,user,**kwargs):
    count=cache.get(key="count",default=1,version=user.id)
    newcount=count+1
    cache.set(key="count",value=newcount,timeout=5,version=user.id)


# @receiver(user_logged_out,sender=User)
# def login_count_signal(sender,request,user,**kwargs):
#     cache.set(key="count",value=1,timeout=10)
#     cache.clear()
