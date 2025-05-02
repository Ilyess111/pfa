from django.urls import path 
from .views import BookingCreateView , BookingListView , BookingDetailView , BookingUpdateView , BookingDeleteView

urlpatterns=[
    # path('new/',BookingCreateView.as_view(),name='booking_create'),
    path("<int:offer_id>/bookings/new/",BookingCreateView.as_view(),name='booking_create'),
    path("bookings/", BookingListView.as_view(), name="bookings_list"),
    path("<int:offer_id>/bookings/<int:pk>/detail/", BookingDetailView.as_view(), name="booking_detail"),
    path("<int:offer_id>/bookings/<int:pk>/edit/", BookingUpdateView.as_view(), name="booking_update"),
    path("<int:offer_id>/bookings/<int:pk>/delete/", BookingDeleteView.as_view(), name="booking_delete"),

]

