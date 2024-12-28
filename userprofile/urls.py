from django.urls import path
from .views import view_profile, edit_profile

urlpatterns = [
    path('v/', view_profile, name='viewp'),
    path('e/', edit_profile, name='editp'),
]
