from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import ParkingSpot, Reservation


def home(request):
    total_spots = ParkingSpot.objects.count()
    available_spots = ParkingSpot.objects.filter(status='available').count()
    occupied_spots = ParkingSpot.objects.filter(status='occupied').count()
    reserved_spots = ParkingSpot.objects.filter(status='reserved').count()

    context = {
        'total_spots': total_spots,
        'available_spots': available_spots,
        'occupied_spots': occupied_spots,
        'reserved_spots': reserved_spots,
    }
    return render(request, 'main/home.html', context)


def parking_map(request):
    spots = ParkingSpot.objects.all().order_by('number')
    return render(request, 'main/parking_map.html', {'spots': spots})


@login_required
def reserve_spot(request, spot_id):
    if request.method == 'POST':
        spot = get_object_or_404(ParkingSpot, id=spot_id)

        if spot.status == 'available':
            # Create reservation
            expires_at = timezone.now() + timedelta(minutes=15)
            Reservation.objects.create(
                user=request.user,
                spot=spot,
                expires_at=expires_at
            )

            # Update spot status
            spot.status = 'reserved'
            spot.save()

            messages.success(request, f'Spot {spot.number} reserved for 15 minutes!')
        else:
            messages.error(request, 'Sorry, this spot is no longer available.')

    return redirect('parking_map')


@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(
        user=request.user,
        is_active=True
    ).order_by('-created_at')

    return render(request, 'main/my_reservations.html', {'reservations': reservations})