from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('certificates/v1/', include('certificates.urls')),
    path('courses/v1/', include('courses.urls')),
    path('progress/v1/', include('progress.urls')),
    path('users/v1/', include('users.urls')),
]
