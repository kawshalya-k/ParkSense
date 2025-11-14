from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('parking-map/', views.parking_map, name='parking_map'),
    path('reserve/<int:spot_id>/', views.reserve_spot, name='reserve_spot'),
    path('my-reservations/', views.my_reservations, name='my_reservations'),
]