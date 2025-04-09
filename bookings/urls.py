from django.urls import path 
from .views import BookingCreateView , BookingListView , BookingDetailView , BookingUpdateView , BookingDeleteView

urlpatterns=[
    path('new/',BookingCreateView.as_view(),name='booking_create'),
    path("", BookingListView.as_view(), name="bookings_list"),
    path("<int:pk>/", BookingDetailView.as_view(), name="booking_detail"),
    path("<int:pk>/edit/", BookingUpdateView.as_view(), name="booking_update"),
    path("<int:pk>/delete/", BookingDeleteView.as_view(), name="booking_delete"),

]

