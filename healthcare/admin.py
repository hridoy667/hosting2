from django.contrib import admin
from .models import DiseaseCategory, HealthcareSuggestion

@admin.register(DiseaseCategory)
class DiseaseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(HealthcareSuggestion)
class HealthcareSuggestionAdmin(admin.ModelAdmin):
    list_display = ('disease_category', 'suggestion', )
    list_filter = ('disease_category',)
    search_fields = ('suggestion',)
