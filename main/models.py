from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class ParkingSpot(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('reserved', 'Reserved'),
    ]

    number = models.CharField(max_length=10)  # e.g., "A1", "B5"
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    location = models.CharField(max_length=100)  # e.g., "Ground Floor", "Level 2"

    def __str__(self):
        return f"Spot {self.number} - {self.status}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - Spot {self.spot.number}"

    def is_expired(self):
        return timezone.now() > self.expires_at
