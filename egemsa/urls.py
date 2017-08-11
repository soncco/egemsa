# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin

import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('front.urls')),
]

admin.site.site_header = 'Transparencia - Administración'
admin.site.site_title = 'Transparencia - Administración'

handler404 = 'front.views.handler404'
handler500 = 'front.views.handler500'
handler403 = 'front.views.handler403'
