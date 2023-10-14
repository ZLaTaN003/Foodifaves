from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    

    email = forms.EmailField()
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

class ProfileUpdate(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['img']
        labels = {
            'img': 'Profile Picture',
        }
        widgets = {
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
