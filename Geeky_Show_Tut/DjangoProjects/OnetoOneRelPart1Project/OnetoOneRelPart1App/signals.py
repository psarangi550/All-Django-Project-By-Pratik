from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import Post #inmporting the models which is the sender
@receiver(signal=post_delete,sender=Post)
def my_recv_function(sender,instance,**kwargs):
    print("POST Delete Signal Working Properly")
    print(kwargs)
    instance.user.delete()
