from django.urls import path
from . import views

urlpatterns = [
    path('', views.features,name="feat"),
]