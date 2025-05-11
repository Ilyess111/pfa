from django import forms
from .models import Booking, Payment


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['num_people', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.SelectDateWidget(years=range(2024, 2035)),
            'end_date': forms.SelectDateWidget(years=range(2024, 2035)),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['card_number', 'card_expiration_date', 'cvv']
        widgets = {
            'card_expiration_date': forms.SelectDateWidget(years=range(2024, 2035)),
        }
        help_texts = {
            'cvv': '3 digits on the back of your card',
        }