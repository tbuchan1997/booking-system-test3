from django.urls import path, include
from . import views

urlpatterns = [
    path('book/', views.book_slot, name='book_slot'),
    path('booking/', include('booking.urls')),
    path('success/', views.booking_success, name='booking_success'),
]