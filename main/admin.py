from django.contrib import admin
from django.utils import timezone
from .models import ParkingSpot, Reservation


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['number', 'status', 'location']
    list_filter = ['status', 'location']
    search_fields = ['number']
    actions = ['make_available']

    def make_available(self, request, queryset):
        count = queryset.update(status='available')
        self.message_user(request, f'{count} spots marked as available')

    make_available.short_description = "Mark selected spots as available"


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'spot', 'created_at', 'expires_at', 'is_active']
    list_filter = ['is_active', 'created_at']
    actions = ['deactivate_reservations']

    def deactivate_reservations(self, request, queryset):
        count = 0
        for reservation in queryset:
            reservation.is_active = False
            reservation.save()

            # Also free the spot
            spot = reservation.spot
            spot.status = 'available'
            spot.save()
            count += 1

        self.message_user(request, f'{count} reservations deactivated and spots freed')

    deactivate_reservations.short_description = "Deactivate and free spots"