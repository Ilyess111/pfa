from django.views.generic import CreateView ,ListView ,DetailView ,UpdateView ,DeleteView
from django.urls import reverse_lazy
from .models import Booking 
from offers.models import Offer
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm # can be deleted if we add the fields attribute 
    template_name = "bookings_templates/booking_form.html"
    success_url = reverse_lazy("bookings_list")
    
    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to make a booking")
        form.instance.user = self.request.user
        return super().form_valid(form)

class BookingListView(ListView):
    model = Booking
    template_name = "bookings_templates/bookings_list.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)  # Show only the user's bookings

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


