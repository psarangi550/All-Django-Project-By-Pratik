from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

@receiver(user_login_failed)
def At_beg_logout(sender,request,credentials,**kwargs):
    print(sender)
    return render(request, "loginlogoutConfirmApp/confirm.html")
