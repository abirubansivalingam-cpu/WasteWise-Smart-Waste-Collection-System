from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import WasteRequest, Complaint
class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=("username","email","password1","password2")
class WasteRequestForm(forms.ModelForm):
    preferred_date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    class Meta:
        model=WasteRequest
        fields=("title","category","description","address","area","quantity_kg","preferred_date","priority")
        widgets={"description":forms.Textarea(attrs={"rows":3})}
class ComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=("subject","details","area")
        widgets={"details":forms.Textarea(attrs={"rows":4})}
