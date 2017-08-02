from django.conf.urls import url

from . import views

app_name = 'front'
urlpatterns = [

    url(r'^$', views.index, name = 'index'),
    url(r'^categoria/(?P<slug>[-\w]+)/$', views.categoria, name = 'categoria'),
    url(r'^documento/(?P<id>.*)$', views.documento, name = 'documento'),
    #url(r'^usuarios$', views.usuarios, name = 'usuarios'),
]
