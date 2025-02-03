from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializer import *


class ProgressView(ListAPIView):
    serializer_class = ProgressSerializer

    def get_queryset(self):
        return Progress.objects.all()
