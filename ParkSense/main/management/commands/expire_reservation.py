from django.core.management.base import BaseCommand
from django.utils import timezone
from main.models import Reservation, ParkingSpot


class Command(BaseCommand):
    help = 'Expire old reservations and free up parking spots'

    def handle(self, *args, **kwargs):
        now = timezone.now()

        # Find expired reservations
        expired = Reservation.objects.filter(
            expires_at__lt=now,
            is_active=True
        )

        count = 0
        for reservation in expired:
            # Deactivate reservation
            reservation.is_active = False
            reservation.save()

            # Make spot available
            spot = reservation.spot
            spot.status = 'available'
            spot.save()

            count += 1
            self.stdout.write(
                self.style.SUCCESS(f'Freed spot {spot.number}')
            )

        self.stdout.write(
            self.style.SUCCESS(f'Expired {count} reservations')
        )