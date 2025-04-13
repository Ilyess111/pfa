from django.db import models

class Offer(models.Model):
    title = models.CharField(max_length=255)  # Name of the offer
    description = models.TextField()  # Detailed description
    destination = models.CharField(max_length=255)  # Where the trip is going
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Cost per person
    duration = models.IntegerField(help_text="Duration in days")  # Number of days
    available_from = models.DateField()  # Start of the availability period
    available_to = models.DateField()  # End of the availability period
    max_people = models.IntegerField(default=1)  # Maximum number of people per booking
    image = models.ImageField(upload_to="offer_images/", blank=True, null=True)  # Image for the offer
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp when created

    def __str__(self):
        return f"{self.title} - {self.destination} (${self.price})"
    
from django.contrib.auth import get_user_model
from django.urls import reverse

class Review(models.Model): 
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE,related_name='reviews')
    title = models.CharField(max_length=255, blank=True, null=True)  # Optional title
    comment = models.CharField(max_length=140)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the review was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the review was last modified
    
    def __str__(self):
        return self.title