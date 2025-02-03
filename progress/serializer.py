from django.core.validators import MaxLengthValidator
from rest_framework import serializers
from .models import *


class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'
