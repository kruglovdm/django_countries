"""DjangoCountries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.main_page),
    path('countries-list', views.countries_page, name='countries-list'),
    path('languages', views.languages_page, name='languages'),
    path('country/<str:country_param>/', views.country_page, name='country'),
    path('countries-list/<str:letter_country_param>/', views.countries_letter_page, name='countries-list-letter'),
    path('countries-language-list/<str:language_country_param>/', views.countries_language_page, name='countries-language-list'),
]

