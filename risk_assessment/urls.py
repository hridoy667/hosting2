from django.urls import path
from . import views

urlpatterns = [
    path('', views.assessments,name="risk-measure"),
]