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