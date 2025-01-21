
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    signature = forms.ImageField(required=False)
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'date_of_birth', 'email', 'password1', 'password2', 'signature', 'role']

    def clean_role(self):
        role = self.cleaned_data.get('role')
        if role == 'Admin' and CustomUser.objects.filter(role='Admin').exists():
            raise forms.ValidationError("An Admin account already exists.")
        return role
