from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('certificates/v1/', include('certificates.urls')),

]
