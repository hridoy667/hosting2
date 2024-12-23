from django import forms
from django.contrib.auth.models import User
from bmiInput.models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [ 'age', 'height_value', 'height_unit', 'weight_value', 'weight_unit', 'weekly_working_hours']

