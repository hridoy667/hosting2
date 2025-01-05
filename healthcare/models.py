from django.db import models


class Season(models.Model):
    name = models.CharField(max_length=50, unique=True)  # e.g., "Summer", "Winter"
    start_month = models.IntegerField()  # e.g., 3 for March
    end_month = models.IntegerField()  # e.g., 5 for May

    def __str__(self):
        return self.name
    

class SeasonalSuggestion(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="seasonal_suggestions")
    detailed_preventive_measures = models.TextField(help_text="Detailed suggestions for preventing seasonal diseases.")
    general_season_tips = models.CharField(max_length=255, help_text="Short tips for general health during the season.")
    additional_seasonal_advice = models.TextField(help_text="Additional health advice for this season.")

    def __str__(self):
        return f"Healthcare suggestion for {self.season.name}"


class SeasonalDisease(models.Model):
    disease_name = models.CharField(max_length=100)  # e.g., "Flu", "Diarrhea"
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="diseases")
    primary_advice = models.TextField()  # e.g., "Stay hydrated, take rest"

    def __str__(self):
        return f"{self.disease_name} ({self.season.name})"


class DiseaseCategory(models.Model):
    """
    Model to represent disease categories.
    """
    name = models.CharField(max_length=50, unique=True)  # e.g., "General", "Heart Disease", "Diabetes"
    description = models.TextField(blank=True, help_text="Optional description for the disease category.")

    class Meta:
        verbose_name = "Disease Category"
        verbose_name_plural = "Disease Categories"
        ordering = ['name']  

    def __str__(self):
        return self.name


class HealthcareSuggestion(models.Model):
    disease_category = models.ForeignKey(
        DiseaseCategory,
        on_delete=models.CASCADE,
        related_name='suggestions',
        help_text="Category of disease this suggestion relates to.",
        null=True, 
        blank=True
    )
    suggestion = models.TextField(help_text="Detailed health suggestion for this disease category.")
    

    class Meta:
        verbose_name = "Healthcare Suggestion"
        verbose_name_plural = "Healthcare Suggestions"
        ordering = ['disease_category']  

    def __str__(self):
        # Display the category and a preview of the suggestion
        return f"{self.disease_category.name}: {self.suggestion[:50]}..." if len(self.suggestion) > 50 else self.suggestion
