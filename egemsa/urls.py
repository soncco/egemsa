from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('front.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Transparencia - Administración'
admin.site.site_title = 'Transparencia - Administración'

handler404 = 'front.views.handler404'
handler500 = 'front.views.handler500'
handler403 = 'front.views.handler403'
