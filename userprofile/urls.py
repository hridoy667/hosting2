from django.urls import path
from .views import view_profile, edit_profile

urlpatterns = [
    path('', view_profile, name='view'),
    path('', edit_profile, name='edit'),
]
