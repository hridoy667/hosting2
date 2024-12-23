from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal, InvalidOperation


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')], default='male')
    height_value = models.DecimalField(max_digits=5, decimal_places=2)
    height_unit = models.CharField(max_length=5, choices=[('m', 'Meters'), ('ft', 'Feet')], default='ft')
    weight_value = models.DecimalField(max_digits=5, decimal_places=2)
    weight_unit = models.CharField(max_length=7, choices=[('kg', 'Kilograms'), ('lb', 'Pounds')], default='kg')
    disease_history = models.CharField(
        max_length=50,
        choices=[
            ('General', 'General'),
            ('Heart Disease', 'Heart Disease'),
        ],
        default='General',
        help_text="Select any pre-existing condition",
    )
    weekly_working_hours = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        try:
           
            if self.height_unit == 'ft':
                feet = int(self.height_value)  
                inches = (self.height_value - feet) * 10  
                total_inches = (feet * 12) + inches  
                self.height_value = Decimal(total_inches) * Decimal('0.0254')  
                self.height_unit = 'm'  

            
            if self.weight_unit == 'lb':
                self.weight_value = Decimal(self.weight_value) * Decimal('0.453592')  
                self.weight_unit = 'kg'  

        except (InvalidOperation, ValueError) as e:
            raise ValueError("Invalid height or weight value entered. Ensure proper numerical format.")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class BMISuggestion(models.Model):
    CATEGORY_CHOICES = [
        ('Underweight', 'Underweight'),
        ('Normal', 'Normal'),
        ('Overweight', 'Overweight'),
        ('Obese', 'Obese')
    ]

    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, unique=True)
    diet_suggestion = models.TextField(default='No diet suggestion available')
    exercise_suggestion = models.TextField(default='No exercise suggestion available')
    water_intake_suggestion = models.TextField(default='No water intake suggestion available')
    sleep_suggestion = models.TextField(default='No sleep suggestion available')
    other_health_tips = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category
