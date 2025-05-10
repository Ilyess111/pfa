from .models import Review
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class ReviewDetailView(DetailView):
    model = Review
    template_name = "reviews_templates/review_detail.html"



class ReviewCreateView(CreateView):
    model = Review
    fields='__all__'
    template_name = "reviews_templates/review_form.html"

    # def form_valid(self, form):
    #     form.instance.author = self.request.user  # Set the author to the current user
    #     form.instance.offer_id = self.kwargs["offer_id"]  # Attach review to offer
    #     return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('review_detail', kwargs={'pk': self.object.pk})

class ReviewUpdateView( UpdateView):
    model = Review
    fields=['title','comment','rating']
    template_name = "reviews_templates/review_form.html"

    # def test_func(self):
    #     review = self.get_object()
    #     return self.request.user == review.user  # Only the author can edit

    def get_success_url(self):
        return reverse_lazy('review_detail', kwargs={'pk': self.object.pk})


class ReviewDeleteView( DeleteView):
    model = Review
    template_name = "reviews_templates/review_confirm_delete.html"

    # def test_func(self):
    #     review = self.get_object()
    #     return self.request.user == review.user  # Only the author can delete

    def get_success_url(self):
        return reverse_lazy('offers_list')
