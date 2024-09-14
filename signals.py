from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time, threading
from django.db import transaction

# Question 1 & 2: Synchronous Signal & Same Thread The answer is given below
@receiver(post_save, sender=User)
def signal_handler(sender, instance, created, **kwargs):
    print(f"Signal received for user: {instance.username}")
    print(f"Signal handler thread: {threading.current_thread().name}")
    time.sleep(5)  # Simulate delay to show synchronous behavior

# Question 3: Signal in Same Transaction The answer is given below
@receiver(post_save, sender=User)
def transaction_handler(sender, instance, created, **kwargs):
    if created:
        print(f"Signal handler: Saving related object for user {instance.username}")
        raise Exception("Error during signal handling")
