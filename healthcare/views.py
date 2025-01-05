from django.shortcuts import render, redirect
from bmiInput.models import UserProfile, BMISuggestion
from django.utils import timezone 
from django.utils.timezone import now
from .models import HealthcareSuggestion, DiseaseCategory
from .models import Season, SeasonalDisease, SeasonalSuggestion
from .models import SeasonalDisease

from .models import Season



def get_current_season():
    current_month = now().month

    # Fetch the current season based on the month
    current_season = None

    # For single-year seasons (e.g., Spring, Summer, Autumn)
    current_season = Season.objects.filter(
        start_month__lte=current_month,
        end_month__gte=current_month
    ).first()

    # If no season found, check for cross-year seasons (e.g., Winter: Dec to Feb)
    if not current_season:
        if current_month == 12:  # December
            current_season = Season.objects.filter(name="Winter").first()
        elif current_month == 1 or current_month == 2:  # January and February
            current_season = Season.objects.filter(name="Winter").first()


    return current_season



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

        # Detect the current season and fetch seasonal diseases
        current_season = get_current_season()
        seasonal_diseases = SeasonalDisease.objects.filter(season=current_season) if current_season else []

        seasonal_healthcare_suggestion = SeasonalSuggestion.objects.filter(season=current_season).first()

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
        'current_season': current_season.name if current_season else "Unknown",
        'seasonal_diseases': seasonal_diseases,
        'seasonal_healthcare_suggestion': seasonal_healthcare_suggestion

    })
