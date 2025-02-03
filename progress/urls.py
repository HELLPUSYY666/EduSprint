from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', ProgressView.as_view(), name='progress-list'),
]
