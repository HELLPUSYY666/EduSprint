from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', CertificateListView.as_view(), name='certificate-list'),
]
