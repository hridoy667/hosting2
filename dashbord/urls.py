from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashbord,name="dashbord"),
    path('m/', views.mindfullness,name="mindfullness"),
]