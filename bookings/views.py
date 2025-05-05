from django.views.generic import CreateView ,ListView ,DetailView ,UpdateView ,DeleteView
from django.urls import reverse_lazy
from .models import Booking  , Payment
from offers.models import Offer
from .forms import BookingForm , PaymentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404


class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm # can be deleted if we add the fields attribute 
    template_name = "bookings_templates/booking_form.html"
    success_url = reverse_lazy("bookings_list")
    
    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to make a booking")

        offer_id = self.kwargs.get("offer_id")
        offer = get_object_or_404(Offer, id=offer_id)
        
        form.instance.user = self.request.user
        form.instance.offer = offer             

        return super().form_valid(form)

class BookingListView(ListView):
    model = Booking
    template_name = "bookings_templates/bookings_list.html"
    context_object_name = "bookings"

    # def get_queryset(self):
    #     return Booking.objects.filter(user=self.request.user)  # Show only the user's bookings

class BookingDetailView(DetailView):
    model = Booking
    template_name = "bookings_templates/booking_detail.html"

class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingForm #we can use the fields attribute to allow the update only for certain fields 
    template_name = "bookings_templates/booking_edit.html"
    success_url = reverse_lazy("bookings_list")

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = "bookings_templates/booking_confirm_delete.html"
    success_url = reverse_lazy("bookings_list")
    
    
# payments views
class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm # can be deleted if we add the fields attribute 
    template_name = "payments_templates/payment_form.html"
    success_url = reverse_lazy("bookings_list")
    
    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to make a payment")

        booking_id = self.kwargs.get("pk")
        booking = get_object_or_404(Booking, id=booking_id)
        
        form.instance.booking = booking        
        form.instance.amount = booking.total_price
        response = super().form_valid(form)
        booking.status="Confirmed"
        booking.save()
        

        return response

# class PaymentListView(ListView):
#     model = Payment
#     template_name = "payments_templates/payments_list.html"
#     context_object_name = "payments"

    # def get_queryset(self):
    #     return Booking.objects.filter(user=self.request.user)  # Show only the user's bookings

class PaymentDetailView(DetailView):
    model = Payment
    template_name = "payments_templates/payment_detail.html"
    
    def get_object(self, queryset=None):
        booking_id = self.kwargs['pk']
        payment_id = self.kwargs['pay_id']
        return get_object_or_404(
            Payment,
            id=payment_id,
            booking_id=booking_id
        )
# class BookingUpdateView(UpdateView):
#     model = Booking
#     form_class = BookingForm #we can use the fields attribute to allow the update only for certain fields 
#     template_name = "bookings_templates/booking_edit.html"
#     success_url = reverse_lazy("bookings_list")

# class BookingDeleteView(DeleteView):
#     model = Booking
#     template_name = "bookings_templates/booking_confirm_delete.html"
#     success_url = reverse_lazy("bookings_list")


