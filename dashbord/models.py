from django.db import models
from bmiInput.models import BMISuggestion


# Time-Based Suggestion Model
class TimeBasedSuggestion(models.Model):
    TIME_PERIOD_CHOICES = [
        ('Morning', '6 AM - 10 AM'),
        ('Midday', '10 AM - 2 PM'),
        ('Afternoon', '2 PM - 6 PM'),
        ('Evening', '6 PM - 10 PM'),
        ('Night', '10 PM - 6 AM'),
    ]
    time_period = models.CharField(max_length=20, choices=TIME_PERIOD_CHOICES)
    bmi_category = models.ForeignKey(BMISuggestion, on_delete=models.CASCADE)  
    diet_suggestion = models.TextField(help_text="Diet suggestions", blank=True)
    Exercise = models.CharField(max_length=150, help_text="Water intake suggestion", blank=True)
    disease = models.CharField(
        max_length=50,
        choices=[
            ('General', 'General'),
            ('Diabetes', 'Diabetes'),
            ('Heart Disease', 'Heart Disease'),
        ],
        help_text="Disease associated with this suggestion",
        default='General'
    )

    def __str__(self):
        return f"{self.time_period} - {self.disease} ({self.bmi_category.category})"


# Time-Based Activity Model
class TimeBasedActivity(models.Model):
    ACTIVITY_CHOICES = [
        ('Deep Work', 'Deep Work'),
        ('Nap', 'Nap'),
        ('Sleep', 'Sleep'),
    ]
    time_period = models.CharField(
        max_length=20,
        choices=[
            ('Morning', '9 AM - 12 PM'),
            ('Afternoon', '1 PM - 3 PM'),
            ('Evening', '3 PM - 5 PM'),
            ('Night', '9 PM - 1 AM'),
        ],
        unique=True
    )
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    suggestion_text = models.TextField()

    def __str__(self):
        return f"{self.activity_type} - {self.time_period}"
