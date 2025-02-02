from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

