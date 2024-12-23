from django.contrib import admin
from .models import TimeBasedSuggestion, TimeBasedActivity



admin.site.register(TimeBasedSuggestion)

@admin.register(TimeBasedActivity)
class TimeBasedActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'time_period')
    list_filter = ('activity_type', 'time_period')
