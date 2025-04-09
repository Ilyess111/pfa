from django.db import models
from users.models import CustomUser
from offers.models import Offer

class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)  # The user who made the booking
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)  # The travel package they booked
    num_people = models.IntegerField(default=1)  # Number of travelers
    start_date = models.DateField()  # Date when the trip starts
    end_date = models.DateField()  # Date when the trip ends
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Total calculated price
    status = models.CharField(
        max_length=20,
        choices=[("Pending", "Pending"), ("Confirmed", "Confirmed"), ("Cancelled", "Cancelled")],
        default="Pending"
    )  # Booking status
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the booking was created




    def __str__(self):
        return f"Booking by {self.user.username} - {self.offer.title} ({self.status})"

    def save(self, *args, **kwargs):
        if self.offer and self.num_people:
            self.total_price = self.num_people * self.offer.price
        super().save(*args, **kwargs)