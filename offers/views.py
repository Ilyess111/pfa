from django.views.generic import ListView , DetailView
from .models import Offer

class OffersListView(ListView):
    model = Offer
    template_name = 'offers_templates/offers_list.html'
    
class OfferDetailView(DetailView): # new
    model = Offer
    template_name = 'offers_templates/offer_detail.html'
    
########


from django.shortcuts import render
from .models import Offer
from .forms import OfferSearchForm

def offer_search(request):
    offers = Offer.objects.all()
    form = OfferSearchForm(request.GET or None)
    
    if form.is_valid():
        # Get the cleaned data from the form
        data = form.cleaned_data
        
        # Apply filters based on the form inputs
        if data.get('title'):
            offers = offers.filter(title__icontains=data['title'])

        if data.get('destination'):
            offers = offers.filter(destination__iexacts=data['destination'])
        
        if data.get('min_duration'):
            offers = offers.filter(duration__gte=data['min_duration'])
        
        if data.get('max_duration'):
            offers = offers.filter(duration__lte=data['max_duration'])
        
        if data.get('max_price'):
            offers = offers.filter(price__lte=data['max_price'])
        
        if data.get('available_from'):
            offers = offers.filter(available_to__gte=data['available_from'])
        
        if data.get('available_to'):
            offers = offers.filter(available_from__lte=data['available_to'])
    
    context = {
        'form': form,
        'offers': offers,
    }
    return render(request, 'offers_templates/offer_search.html', context)
