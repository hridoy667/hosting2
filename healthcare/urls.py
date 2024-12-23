from django.urls import path
from . import views

urlpatterns = [
    path('', views.healthcare_view, name='healthcare'),
]
