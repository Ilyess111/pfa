from datetime import datetime, timezone
from zoneinfo import ZoneInfo
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
    form_class = BookingForm
    template_name = "bookings_templates/booking_form.html"
    success_url = reverse_lazy("bookings_list")
    
    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to make a booking")

        # Get the offer
        offer_id = self.kwargs.get("offer_id")
        offer = get_object_or_404(Offer, id=offer_id)
        
        # Get form data
        num_people = form.cleaned_data.get('num_people')
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')

        # Validate num_people
        if num_people <= 0:
            form.add_error('num_people', "Number of people must be at least 1.")
        elif num_people > offer.max_people:
            form.add_error(
                'num_people',
                f"Cannot book for {num_people} people. Maximum allowed is {offer.max_people}."
            )

        # Validate dates
        if start_date and end_date and start_date >= end_date:
            form.add_error('end_date', "End date must be after start date.")

        # If there are any errors, return form_invalid
        if form.errors:
            return self.form_invalid(form)

        # Set the user and offer if validation passes
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
        
           # Additional validation in the view
        cvv = form.cleaned_data.get('cvv')
        expiration_date = form.cleaned_data.get('card_expiration_date')
        
        # Validate card is not expired (redundant check for extra safety)
        if expiration_date and expiration_date < datetime.now(ZoneInfo("America/New_York")):
            form.add_error('card_expiration_date', "Card has expired")
            return self.form_invalid(form)
            
        # # Validate card number passes Luhn algorithm (basic check)
        # if not self.luhn_check(str(card_number)):
        #     form.add_error('card_number', "Invalid card number")
        #     return self.form_invalid(form)
        
        if len(cvv)!=3:
            form.add_error('cvv', "Invalid cvv")
            return self.form_invalid(form)
        

        
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


