from django.contrib import admin
from .models import Offer , Review
from bookings.models import Booking

class ReviewInline(admin.TabularInline): # new
    model = Review
    extra = 0
    
class BookingInline(admin.TabularInline): # new
    model = Booking
    extra = 0
    
class OfferAdmin(admin.ModelAdmin): # new
    inlines = [
    ReviewInline,BookingInline
]
    list_display = ['id', '__str__'] 
    
class ReviewAdmin(admin.ModelAdmin): # new
    list_display = ['id', '__str__'] 


admin.site.register(Offer,OfferAdmin)
admin.site.register(Review,ReviewAdmin)