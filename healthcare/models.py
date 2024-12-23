from django.db import models


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
