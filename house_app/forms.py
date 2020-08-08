from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import House,WareHouse,Land



class RegistrationForm(UserCreationForm):
    email=forms.CharField(max_length=80)
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class HouseCreationForm(forms.ModelForm):
    class Meta:
        model=House
        fields=['name','location','price','bathrooms','bedrooms',
                'toilets','sitting_room','swimming_pool','image1']
    

class LandCreationForm(forms.ModelForm):
    class Meta:
        model=Land
        fields=['location','space','price']


class WareHouseCreationForm(forms.ModelForm):
    class Meta:
        model=WareHouse
        fields=['name','location','price','space']