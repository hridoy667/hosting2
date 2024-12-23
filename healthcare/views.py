from django.shortcuts import render, redirect
from bmiInput.models import UserProfile, BMISuggestion
from .models import HealthcareSuggestion, DiseaseCategory

def healthcare_view(request):
    if not request.user.is_authenticated:
        return redirect('signin')

    try:
        user_profile = UserProfile.objects.get(user=request.user)

        
        bmi = round(user_profile.weight_value / (user_profile.height_value ** 2), 2)
        bmi_category = BMISuggestion.objects.filter(
            category=(
                'Underweight' if bmi < 18.5 else
                'Normal' if 18.5 <= bmi < 25 else
                'Overweight' if 25 <= bmi < 30 else
                'Obese'
            )
        ).first()

        
        disease_category = DiseaseCategory.objects.filter(name=user_profile.disease_history).first()
        healthcare_suggestions = HealthcareSuggestion.objects.filter(disease_category=disease_category)

    except UserProfile.DoesNotExist:
        return render(request, 'healthcare/healthcare.html', {
            'error': 'Your profile information is incomplete. Please complete your profile.',
            'healthcare_suggestions': [],
        })

    return render(request, 'healthcare/healthcare.html', {
        'disease_category': disease_category,
        'healthcare_suggestions': healthcare_suggestions,
        'bmi': bmi,
        'bmi_category': bmi_category,
    })
