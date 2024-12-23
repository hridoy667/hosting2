from django.urls import path
from . import views

urlpatterns = [
    path('bmin/<int:user_id>/', views.bmiIn,name='bIn'),
]