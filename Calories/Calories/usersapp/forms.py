from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

from Calories.usersapp.models import Profile


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'username':
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = 'Enter Username'
            elif name == 'password1':
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = 'Enter Password'
            elif name == 'password2':
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = 'Confirm Password'
                field.help_text = ''

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'username':
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = 'Enter Username'
            elif name == 'password':
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = 'Enter Password'


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'old_password':
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = 'Enter Old Password'
            elif name == 'new_password1':
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = 'Enter New Password'
            elif name == 'new_password2':
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = 'Confirm New Password'


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

