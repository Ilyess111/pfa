from django import forms
from .models import Booking, Payment


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['num_people', 'start_date', 'end_date']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['card_number', 'card_expiration_date', 'cvv']