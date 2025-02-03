from django.core.validators import MaxLengthValidator
from rest_framework import serializers
from .models import *


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'
