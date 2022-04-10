from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from Calories.usersapp.models import Profile


class UserForm(UserCreationForm):
    username = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Enter Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Enter Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Confirm Password'})
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'age', 'weight', 'height', 'activity_level', 'sex', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Enter Last Name'}),
            'image': forms.FileInput(attrs={'placeholder': 'Add Picture'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Enter Email'}),
            'age': forms.NumberInput(attrs={'class': 'form-control',
                                            'placeholder': 'Enter Age'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control',
                                               'placeholder': 'Enter Weight in kg'}),
            'height': forms.NumberInput(attrs={'class': 'form-control',
                                               'placeholder': 'Enter Height in cm'}),
            'activity_level': forms.Select(attrs={'class': 'form-control',
                                                  'placeholder': 'Enter Gender'},
                                           choices=Profile.ACTIVITY_LEVEL_CHOICES),
            'sex': forms.Select(attrs={'class': 'form-control',
                                       'placeholder': 'Enter Gender'},
                                choices=Profile.GENDER_CHOICES)
        }
