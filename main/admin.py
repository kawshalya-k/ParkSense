from django.contrib import admin
from .models import ParkingSpot, Reservation

@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['number', 'status', 'location']
    list_filter = ['status', 'location']
    search_fields = ['number']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'spot', 'created_at', 'expires_at', 'is_active']
    list_filter = ['is_active', 'created_at']