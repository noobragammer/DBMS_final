from django import forms
from django.core.exceptions import ValidationError
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your username'
    }))
    password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password'
    }))


class RegistrationForm(forms.ModelForm):
    
    password = forms.CharField(
        max_length=255,
        min_length=8,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter a secure password'}),
        help_text="Password must be at least 8 characters long."
    )
    confirm_password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'contact_number', 'email_address', 'password', 'signature', 'role']

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if len(contact_number) != 11 or not contact_number.isdigit():
            raise ValidationError("Contact number must be exactly 11 digits.")
        return contact_number

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data


class ForgotPasswordForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your username'
    }))
    password = forms.CharField(
        max_length=255,
        min_length=8,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter a new password'}),
        help_text="Password must be at least 8 characters long."
    )
    confirm_password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your new password'}),
        label="Confirm Password"
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data
