from django.db.models.signals import pre_migrate,post_migrate
from django.dispatch import receiver


#here we are writing the receiver function
@receiver(signal=pre_migrate)
def before_migrate_signal(sender,**kwargs):
    print("******************************")
    print("Sender",sender)
    print("Arguments",kwargs)
    print("******************************")

@receiver(signal=post_migrate)
def before_migrate_signal(sender,**kwargs):
    print("******************************")
    print("Sender",sender)
    print("Arguments",kwargs)
    print("******************************")
