from django.db.models.signals import pre_save,pre_init,post_init,pre_delete
from django.dispatch import receiver
from .models import Student
from django.utils.text import slugify
from django.shortcuts import HttpResponseRedirect
@receiver(post_init,sender=Student)
def before_save_generator(sender,instance,*args,**kwargs):
    # print(sender)
    instance.identifier=slugify(instance.name)



@receiver(pre_delete,sender=Student)
def before_save_generator(sender,instance,*args,**kwargs):
    return HttpResponseRedirect("/confirm/")
    # print(sender)
    # instance.identifier=slugify(instance.name)
