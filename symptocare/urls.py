"""
URL configuration for symptocare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Landing_page import views
from Landing_page.views import landing


urlpatterns = [
    path('admin/',admin.site.urls),
    path('',landing,name='landing'),
    path('su/', include('signup.urls')),
    path('dashbord/', include('dashbord.urls')),
    path('signin/', include('signin.urls')),
    path('bm/', include('bmiInput.urls')),
    path('about/', include('about_us.urls')),
    path('contact/', include('contact_us.urls')),
    path('f/', include('features.urls')),
    path('userprofile/', include('userprofile.urls')),
    path('diagnose/', include('diagnosis.urls')), 
    path('healthcare/', include('healthcare.urls')), 
]
