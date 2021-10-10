from django.db.models.signals import pre_init,post_init,pre_save,post_save,pre_delete,post_delete,class_prepared
from django.dispatch import receiver
from .models import Student,Employee


# @receiver(class_prepared)
# def diplay_model(sender,**kwargs):
#     print(f"sender:-{sender}")
#     print(f"argument:-{kwargs}")


# @reciver(signal=pre_save,sender=Student)
# def before_model_save(sender,instance,**kwargs):
#     print(f'sender:-{sender}')
#     print(f'instance:-{instance}')
#     instance.regi=instance.roll
#     print(f"Arguments:-{kwargs}")
# pre_save.connect(before_model_save,sender=Employee)

# @receiver(post_save,sender=Employee)
# def after_model_save_created(sender,instance,created,**kwargs):
#     if created==True:
#         print("This is a New Record")
#         print("###################################################")
#         print(f'sender:-{sender}')
#         print(f'instance:-{instance}')
#         print(f'instance ID:-{instance.id}')
#         print(f'instance Roll:-{instance.roll}')
#         print(f'instance Name:-{instance.name}')
#         print(f'instance Mark:-{instance.marks}')
#         print(f'instance Regi:-{instance.regi}')
#         print(f" Arguments:-{kwargs}")
#         print("###################################################")
#     else:
#         print("This is a Updated Record")
#         print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#         print(f'sender:-{sender}')
#         print(f'instance:-{instance}')
#         print(f'instance ID:-{instance.id}')
#         print(f'instance Roll:-{instance.roll}')
#         print(f'instance Name:-{instance.name}')
#         print(f'instance Mark:-{instance.marks}')
#         print(f'instance Regi:-{instance.regi}')
#         print(f" Arguments:-{kwargs}")
#         print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

# @receiver(signal=pre_delete, sender=    Employee)
# def before_delete_record(sender,instance,**kwargs):
#     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#     print(f"sender:-->{sender}")
#     print(f"Instance:-->{instance}")
#     print(f"Arguments:-->{kwargs}")
#     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# @receiver(signal=post_delete, sender=Employee)
# def after_delete_record(sender,instance,**kwargs):
#     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#     print(f"sender:-->{sender}")
#     print(f"Instance:-->{instance}")
#     print(f"Arguments:-->{kwargs}")
#     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

@receiver(signal=pre_init, sender=Employee)
def before_model_created(sender,**kwargs):
    print("*****************************************************************")
    print(f"sender:-->{sender}")
    print(f"Arguments:-->{kwargs}")
    print("*****************************************************************")

@receiver(signal=post_init, sender=Employee)
def before_model_created(sender,instance,**kwargs):
    print("*****************************************************************")
    print("POST INIT Description")
    print(f"sender:-->{sender}")
    print(f"Instance:-->{instance}")
    print(f"Arguments:-->{kwargs}")
    print("*****************************************************************")



