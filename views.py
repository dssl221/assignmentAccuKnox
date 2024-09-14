import threading
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.db import transaction

def create_user_view():
    # For Question 1 & 2: Synchronous Signals
    print(f"Main thread: {threading.current_thread().name}")
    new_user = User.objects.create(username='testuser', password='testpass')
    print("User creation completed")

    # For Question 3: Signal in Same Transaction
    try:
        with transaction.atomic():
            new_user = User.objects.create(username='testuser2', password='testpass2')
    except Exception as e:
        print(f"Exception caught: {e}")

    print("Does the user exist in the database?")
    print(User.objects.filter(username='testuser2').exists())

