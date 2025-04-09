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