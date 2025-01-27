from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['equipment_name', 'equipment_category', 'technician_name', 'priority']
        widgets = {
            'equipment_name': forms.TextInput(attrs={'placeholder': 'Enter equipment name'}),
            'equipment_category': forms.Select(),
            'technician_name': forms.TextInput(attrs={'placeholder': 'Enter technician name (optional)'}),
            'priority': forms.Select(),
        }
