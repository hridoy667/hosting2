from django.urls import path
from .views import view_profile, edit_profile

urlpatterns = [
    path('viewprofile/', view_profile, name='view'),
    path('editprofile/', edit_profile, name='edit'),
]
