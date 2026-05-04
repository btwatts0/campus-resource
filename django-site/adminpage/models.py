from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Resource(models.Model):
    CATEGORY_CHOICES = [
        ("Books", "Books"),
        ("Rooms", "Rooms"),
        ("Loanables", "Loanables"),
        ("Tutoring", "Tutoring"),
    ]

    AVAILABILITY_CHOICES = [
        ("Available", "Available"),
        ("Limited", "Limited"),
        ("Unavailable", "Unavailable"),
    ]

    name = models.CharField(max_length = 200)
    category = models.CharField(max_length = 20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=200)
    desc = models.TextField()
    avail = models.CharField(max_length = 20, choices=AVAILABILITY_CHOICES)

class Reservation(models.Model):
    TIME_SLOTS = [
        ("8:00 AM", "8:00 AM"),
        ("9:00 AM", "9:00 AM"),
        ("10:00 AM", "10:00 AM"),
        ("11:00 AM", "11:00 AM"),
        ("12:00 PM", "12:00 PM"),
        ("1:00 PM", "1:00 PM"),
        ("2:00 PM", "2:00 PM"),
        ("3:00 PM", "3:00 PM"),
        ("4:00 PM", "4:00 PM"),
        ("5:00 PM", "5:00 PM"),
        ("6:00 PM", "6:00 PM"),
        ("7:00 PM", "7:00 PM"),
    ]

    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    timeSlot = models.CharField(max_length = 20, choices = TIME_SLOTS)
    timeReserved = models.CharField(max_length = 200)