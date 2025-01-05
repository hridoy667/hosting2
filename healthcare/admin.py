from django.contrib import admin
from .models import DiseaseCategory, HealthcareSuggestion
from .models import Season, SeasonalDisease, SeasonalSuggestion 

@admin.register(DiseaseCategory)
class DiseaseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(HealthcareSuggestion)
class HealthcareSuggestionAdmin(admin.ModelAdmin):
    list_display = ('disease_category', 'suggestion', )
    list_filter = ('disease_category',)
    search_fields = ('suggestion',)

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_month', 'end_month')
    search_fields = ('name',)


@admin.register(SeasonalDisease)
class SeasonalDiseaseAdmin(admin.ModelAdmin):
    list_display = ('disease_name', 'season', 'primary_advice')
    list_filter = ('season',)
    search_fields = ('disease_name',)

admin.site.register(SeasonalSuggestion)