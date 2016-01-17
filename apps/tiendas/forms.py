from django import forms
from .models import Tienda, Zona, UserProfile
from django.contrib.auth.models import User



class ZonaForm(forms.ModelForm):
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Zona
        fields = ('nombre', 'localizacion','imagen')


class TiendaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Please enter the category name.")
    calle = forms.CharField(max_length=128)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tienda
        exclude = ('zona',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')