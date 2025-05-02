from django import forms
from .models import Booking , Offer

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields =['num_people','start_date','end_date']
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['offer'].queryset = Offer.objects.all()  # Populate offer options
