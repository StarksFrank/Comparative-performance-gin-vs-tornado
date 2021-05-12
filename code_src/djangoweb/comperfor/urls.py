from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('user/', home, name='home'),
]