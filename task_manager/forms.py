from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['equipment_name', 'equipment_category', 'technician_name', 'priority', 'comment'] 
        widgets = {
            'equipment_name': forms.TextInput(attrs={'placeholder': 'Enter equipment name'}),
            'equipment_category': forms.Select(),
            'technician_name': forms.TextInput(attrs={'placeholder': 'Enter technician name (optional)'}),
            'priority': forms.Select(),
            'comment': forms.Textarea(attrs={'placeholder': 'Enter your comment here', 'rows': 4, 'cols': 40}),  
            'status': forms.Select(),
        }
