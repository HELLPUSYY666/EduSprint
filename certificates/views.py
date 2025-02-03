from rest_framework.generics import ListAPIView
from django.shortcuts import render
from certificates.models import Certificate
from .serializer import CertificateSerializer


class CertificateListView(ListAPIView):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        return Certificate.objects.all()