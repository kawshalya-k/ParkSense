from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),  # Landing page (public)
    path('home/', views.home, name='home'),  # Dashboard (after login)
    path('about/', views.about, name='about'),  # About page
    path('parking-map/', views.parking_map, name='parking_map'),
    path('reserve/<int:spot_id>/', views.reserve_spot, name='reserve_spot'),
    path('my-reservations/', views.my_reservations, name='my_reservations'),
    path('cancel-reservation/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
    path('profile/', views.profile, name='profile'),  # User profile
    path('signup/', views.signup, name='signup'),
]