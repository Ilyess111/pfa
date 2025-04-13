from django.contrib import admin
from .models import Offer , Review

class ReviewInline(admin.TabularInline): # new
    model = Review
    
class OfferAdmin(admin.ModelAdmin): # new
    inlines = [
    ReviewInline,
]

admin.site.register(Offer)
admin.site.register(Review)