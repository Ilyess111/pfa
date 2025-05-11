from django.views.generic import ListView , DetailView , CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Offer , Review

class OffersListView(ListView):
    model = Offer
    template_name = 'offers_templates/offers_list.html'
    
class OfferDetailView(DetailView): # new
    model = Offer
    template_name = 'offers_templates/offer_detail.html'
    pk_url_kwarg = 'offer_id'
    
########


from django.shortcuts import render
from .models import Offer
from .forms import OfferSearchForm

def offer_search(request):
    offers = Offer.objects.all()
    form = OfferSearchForm(request.GET or None)
    
    if form.is_valid():
        data = form.cleaned_data
        
        if data.get('title'):
            offers = offers.filter(title__icontains=data['title'])
        
        if data.get('destination'):
            offers = offers.filter(destination__icontains=data['destination'])
        
        if data.get('min_duration'):
            offers = offers.filter(duration__gte=data['min_duration'])
        
        if data.get('max_duration'):
            offers = offers.filter(duration__lte=data['max_duration'])
        
        if data.get('min_price'):
            offers = offers.filter(price__gte=data['min_price'])
        
        if data.get('max_price'):
            offers = offers.filter(price__lte=data['max_price'])
        
        if data.get('available_from') and data.get('available_to'):
            offers = offers.filter(
                available_from__lte=data['available_to'],
                available_to__gte=data['available_from']
            )
        else:
            if data.get('available_from'):
                offers = offers.filter(available_to__gte=data['available_from'])
            if data.get('available_to'):
                offers = offers.filter(available_from__lte=data['available_to'])



    context = {
        'form': form,
        'offers': offers,
    }
    return render(request, 'offers_templates/offer_search.html', context)

# reviews related views

class ReviewsListView(ListView):
    model=Review
    template_name="offers_templates/offer_detail.html"
    # context_object_name = 'all_reviews'

#maybe we'll remove it (not a good functionnality)
class ReviewDetailView(DetailView):
    model = Review
    template_name = "reviews_templates/review_detail.html"
    pk_url_kwarg = 'review_id'



class ReviewCreateView(CreateView):
    model = Review
    fields=['title','comment','rating']
    template_name = "reviews_templates/review_form.html"
    
    def form_valid(self, form):
        """Automatically set the author and offer before saving"""
        form.instance.author = self.request.user
        form.instance.offer_id = self.kwargs['offer_id'] #self.kwargs is a dictionary that contains URL pattern
        return super().form_valid(form)
    
    def get_success_url(self):
        """Redirect to offer detail page after successful submission"""
        return reverse_lazy('offer_detail', kwargs={'offer_id': self.kwargs['offer_id']})

class ReviewUpdateView( UpdateView):
    model = Review
    fields=['title','comment','rating']
    template_name = "reviews_templates/review_form.html"
    pk_url_kwarg = 'review_id'


    def get_success_url(self):
        return reverse_lazy('review_detail', kwargs={
            'offer_id': self.object.offer.id,  
            'review_id': self.object.id      
        })


class ReviewDeleteView( DeleteView):
    model = Review
    template_name = "reviews_templates/review_confirm_delete.html"
    pk_url_kwarg = 'review_id'

    def get_success_url(self):
        return reverse_lazy('offers_list')

