"""
remover_ml URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("remover_ml.urls"))
]
