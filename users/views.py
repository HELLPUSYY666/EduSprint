from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView

from .serializer import UserSerializer
from .service import send_welcome_email
from .tasks import send_welcome_email
from rest_framework.generics import ListAPIView


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'users/usercreate.html'

    def form_valid(self, form):
        form.save()
        # send_welcome_email(form.instance.email)
        send_welcome_email.delay(form.instance.email)
        return super().form_valid(form)


class UserListView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
