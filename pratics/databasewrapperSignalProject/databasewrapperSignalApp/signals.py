from django.db.backends.signals import connection_created
from django.dispatch import receiver

@receiver(signal=connection_created)
def Database_Connection_Signal(sender,connection,**kwargs):
    print("***********************************")
    print(f"sender:-{sender}")
    print(f"Argument:-{kwargs}")
    print(f"Connection:-{connection}")
    print("***********************************")
