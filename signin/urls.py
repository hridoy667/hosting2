from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin,name='signin'),

    path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user,name='logout'),
]