from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_slot, name='book_slot'),
    path('success/', views.booking_success, name='booking_success'),
]
