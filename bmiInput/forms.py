# bmiInput/forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'gender', 'height_value', 'height_unit', 'weight_value', 'weight_unit', 'disease_history', 'weekly_working_hours']
        
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'height_value': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Write 5 feet 4 inches as 5.4'}),
            'height_unit': forms.Select(attrs={'class': 'form-select'}),
            'weight_value': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter weight'}),
            'weight_unit': forms.Select(attrs={'class': 'form-select'}),
            'disease_history': forms.Select(attrs={'class': 'form-select'}),
            'weekly_working_hours': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter weekly working hours'}),
        }

    def clean_height_value(self):
        height = self.cleaned_data['height_value']
        if height <= 0:
            raise forms.ValidationError("Height must be a positive number.")
        return height

    def clean_weight_value(self):
        weight = self.cleaned_data['weight_value']
        if weight <= 0:
            raise forms.ValidationError("Weight must be a positive number.")
        return weight
