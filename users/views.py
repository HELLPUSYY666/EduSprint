from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser

from .serializer import UserSerializer, UsersDetailSerializer
from .tasks import send_welcome_email


class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'users/usercreate.html'

    def form_valid(self, form):
        form.save()
        send_welcome_email.delay(form.instance.email)
        return super().form_valid(form)


class UserListView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetailView(APIView):
    def get(self, request, pk):
        try:
            user = CustomUser.objects.get(id=pk)
        except CustomUser.DoesNotExist:
            return Response({'detail': 'User not found'}, status=404)

        serializer = UsersDetailSerializer(user)
        return Response(serializer.data)
