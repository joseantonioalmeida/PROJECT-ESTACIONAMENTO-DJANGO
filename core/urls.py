from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('customers.urls')),
    path('api/v1/', include('parking.urls')),
    ]

if settings.DEBUG:
    import os
    # Servir arquivos estáticos em desenvolvimento
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=os.path.join(settings.BASE_DIR, 'static')
    )
