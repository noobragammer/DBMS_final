from django import forms
from .models import Equipment

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'owner', 'category', 'frequency', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter equipment name', 'class': 'form-control'}),
            'owner': forms.TextInput(attrs={'placeholder': 'Enter owner name', 'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'frequency': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
