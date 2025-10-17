import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import DummyModel

@receiver(post_save, sender=DummyModel)
def slow_signal_handler(sender, instance, **kwargs):
    print("Signal handler started...")
    time.sleep(1)
    print("Signal handler completed!")

@receiver(post_save, sender=DummyModel)
def thread_check_handler(sender, instance, **kwargs):
    print("Signal running in thread:", threading.get_ident())

@receiver(post_save, sender=DummyModel)
def transaction_check_handler(sender, instance, **kwargs):
    print("Signal inside atomic block:", transaction.get_connection().in_atomic_block)
