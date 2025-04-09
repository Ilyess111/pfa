
from django import forms
from django.forms import DateInput

class OfferSearchForm(forms.Form):
    title = forms.CharField(required=False)
    destination = forms.CharField(required=False)
    min_duration = forms.IntegerField(required=False, label="Minimum duration (days)")
    max_duration = forms.IntegerField(required=False, label="Maximum duration (days)")
    max_price = forms.DecimalField(required=False, decimal_places=2)
    available_from = forms.DateField(required=False, widget=DateInput(attrs={'type': 'date'}))
    available_to = forms.DateField(required=False, widget=DateInput(attrs={'type': 'date'}))