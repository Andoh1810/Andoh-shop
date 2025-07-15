#importation des modules nécessaires de django
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Mot de passe", 
        strip=False, #permet de desactiver la suppression automatique des espaces au tour du mot de passe
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}), #nous avons utilisé un widget de mot de passe avec attributs spécifiques
    )

    password2 = forms.CharField(
        label= "Confirmation du mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),
    )


    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1", "password2")