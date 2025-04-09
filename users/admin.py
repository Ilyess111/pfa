from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CutsomUserCreationForm , CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form=CutsomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    #list_display for admin panel's table of users fields .
    list_display=['username','email','is_staff']
    #fieldsets for edit , add_fieldsets for creation.
    fieldsets = (
        (None, {'fields': ('username', 'password')}),  
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'is_staff', 'is_active')}
        ),
    )
    
admin.site.register(CustomUser,CustomUserAdmin)