from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm , CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    #list_display for admin panel's table of users fields .
    list_display=['username','email','phone_number','date_of_birth']
    #fieldsets for edit , add_fieldsets for creation.
    fieldsets = (
        (None, {'fields': ('username', 'password')}),  
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2','email','phone_number','date_of_birth')}
        ),
    )
    
admin.site.register(CustomUser,CustomUserAdmin)