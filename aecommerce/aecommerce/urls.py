from django.contrib import admin
from django.urls import (
    path,
    include
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('apiapp.urls', namespace='api')),
    path('', include('mainapp.urls', namespace='main')),
    path('acc/', include('accountsapp.urls', namespace='accounts'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    ) + static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )


