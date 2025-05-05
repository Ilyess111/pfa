from django.urls import path 
from .views import (BookingCreateView , BookingListView , BookingDetailView , BookingUpdateView , BookingDeleteView,
                    PaymentCreateView,PaymentListView,PaymentDetailView
                    )

urlpatterns=[
    # path('new/',BookingCreateView.as_view(),name='booking_create'),
    path("<int:offer_id>/bookings/new/",BookingCreateView.as_view(),name='booking_create'),
    path("bookings/", BookingListView.as_view(), name="bookings_list"),
    path("bookings/<int:pk>/detail/", BookingDetailView.as_view(), name="booking_detail"),
    path("bookings/<int:pk>/edit/", BookingUpdateView.as_view(), name="booking_update"),
    path("bookings/<int:pk>/delete/", BookingDeleteView.as_view(), name="booking_delete"),
    # payments urls
    path("<int:offer_id>/bookings/<int:pk>/payments/new/", PaymentCreateView.as_view(), name="pay_create"),
    # path("bookings/<int:pk>/payments/", PaymentListView.as_view(), name="pays_list"),
    path("bookings/<int:pk>/payments/<int:pay_id>/detail/", PaymentDetailView.as_view(), name="pay_detail"),

]

