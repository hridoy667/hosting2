from django.urls import path
from . import views

urlpatterns = [
    
    path('suf/', views.registryForm, name='signup'),
]