from django.db import models

class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    destination = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in days", editable=False)  
    available_from = models.DateField()
    available_to = models.DateField()
    max_people = models.IntegerField(default=1)
    image = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.destination} (${self.price})"
    
    def save(self, *args, **kwargs):
        # Calculate duration before saving
        if self.available_from and self.available_to:
            self.duration = (self.available_to - self.available_from).days + 1  
        super().save(*args, **kwargs)
    
from django.contrib.auth import get_user_model
from django.urls import reverse

class Review(models.Model): 
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE,related_name='reviews')
    title = models.CharField(max_length=255, blank=True, null=True)  # Optional title
    comment = models.CharField(max_length=140)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the review was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the review was last modified
    
    def __str__(self):
        return self.title