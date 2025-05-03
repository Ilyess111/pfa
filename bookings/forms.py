from django import forms
from .models import Booking , Payment

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields =['num_people','start_date','end_date']
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['offer'].queryset = Offer.objects.all()  # Populate offer options

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields =['card_number','card_expiration_date','cvv']
    # full_name = forms.CharField(label="Full Name", max_length=100)
    # card_number = forms.CharField(label="Card Number", max_length=16, widget=forms.PasswordInput)
    # card_expiration_date = forms.DateField(label="Expiration Date", widget=forms.DateInput(attrs={'type': 'date'}))
    # cvv = forms.CharField(label="CVV", max_length=4, widget=forms.PasswordInput)
    # amount = forms.DecimalField(label="Amount", max_digits=10, decimal_places=2)
