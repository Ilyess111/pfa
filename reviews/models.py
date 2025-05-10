from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from offers.models import Offer

# Create your models here.
class Review(models.Model): # new
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE,related_name='reviews')
    title = models.CharField(max_length=255, blank=True, null=True)  # Optional title
    comment = models.CharField(max_length=140)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the review was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the review was last modified
    
    def __str__(self):
        return self.title