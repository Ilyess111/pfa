from django.contrib import admin
from .models import Booking , Payment 

class BookingAdmin(admin.ModelAdmin): 
     list_display = ['id', '__str__'] 
     
class PaymentAdmin(admin.ModelAdmin):
     list_display=['id', '__str__']

admin.site.register(Booking,BookingAdmin)
admin.site.register(Payment,PaymentAdmin)
