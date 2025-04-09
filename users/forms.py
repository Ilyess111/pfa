from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser

class CutsomUserCreationForm (UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields=UserCreationForm.Meta.fields+('email','phone_number','date_of_birth',)
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=UserCreationForm.Meta.fields