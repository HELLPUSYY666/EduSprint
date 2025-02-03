from django.urls import path, include
from .views import *
urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('user/create/', UserCreateView.as_view(), name='user-create'),
]
