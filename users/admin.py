from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class UserAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = User
        fields = '__all__'


class CustomUserAdmin(UserAdmin):
    form = UserAdminForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('content',)}),
    )


if not admin.site.is_registered(User):
    admin.site.register(User, CustomUserAdmin)
