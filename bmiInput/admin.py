from django.contrib import admin


# Register your models here.
from django.contrib import admin
from .models import UserProfile, BMISuggestion

@admin.register(BMISuggestion)

class BMISuggestionAdmin(admin.ModelAdmin):
    list_display = ('category', 'diet_suggestion', 'exercise_suggestion', 'water_intake_suggestion')
    search_fields = ('category',)
    