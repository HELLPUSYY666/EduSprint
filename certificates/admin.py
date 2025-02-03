from django.contrib import admin
from certificates.models import Certificate

if not admin.site.is_registered(Certificate):
    admin.site.register(Certificate)
