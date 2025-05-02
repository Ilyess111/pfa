from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin): # new
     list_display = ['id', '__str__'] 

admin.site.register(Booking,BookingAdmin)
