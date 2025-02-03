from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# остальной код без изменений
urlpatterns = [
    path('admin/', admin.site.urls),
    path('certificates/', include('certificates.urls')),
    path('courses/', include('courses.urls')),
    path('progress/', include('progress.urls')),
    path('users/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

