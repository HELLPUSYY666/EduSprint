from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Certificate


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'
