from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime
from bmiInput.models import UserProfile, BMISuggestion
from .models import TimeBasedSuggestion, TimeBasedActivity

# Calculate BMI
def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obese'

def mindfullness(request):
        return render(request, 'dashbord/mindfullness.html')

def dashbord(request):
    if request.user.is_authenticated:
        try:
            # Fetch the user's profile
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return render(request, 'dashbord/dashbord.html', {'error': 'Profile not found'})

        # Extract user-specific details
        height = user_profile.height_value
        weight = user_profile.weight_value
        disease_history = user_profile.disease_history or "General"

        # Calculate BMI category
        bmi_category = calculate_bmi(height, weight)

        # Fetch BMI-based suggestions
        try:
            suggestion = BMISuggestion.objects.get(category=bmi_category)
        except BMISuggestion.DoesNotExist:
            suggestion = None

        other_health_tips = suggestion.other_health_tips if suggestion else "No additional tips available."

        # Determine current time period
        current_hour = timezone.localtime().hour
        if 5 <= current_hour < 11:
            current_time_period = "Morning"
        elif 11 <= current_hour < 13:
            current_time_period = "Midday"
        elif 13 <= current_hour < 17:
            current_time_period = "Afternoon"
        elif 17 <= current_hour < 19:
            current_time_period = "Evening"
        else:
            current_time_period = "Night"

        # Fetch only the current time period's suggestion
        current_suggestion = TimeBasedSuggestion.objects.filter(
            bmi_category__category=bmi_category, 
            disease=disease_history,
            time_period=current_time_period
        ).first()

        # Fetch time-based activities (e.g., Deep Work, Nap)
        time_based_activities = TimeBasedActivity.objects.filter(
            time_period=current_time_period
        )

        #greeting section

        if 5 <= current_hour < 12:
            greeting = "Good Morning"
        elif 12 <= current_hour < 17:
            greeting = "Good Afternoon"
        elif 17 <= current_hour < 21:
            greeting = "Good Evening"
        else:
            greeting = "Good Night"


        return render(request, 'dashbord/dashbord.html', {
            'suggestion': suggestion,
            'current_time_period': current_time_period,
            'current_suggestion': current_suggestion,
            'time_based_activities': time_based_activities,
            'greeting': greeting,
            'other_health_tips':other_health_tips,

        })

    return redirect('signin')

    
