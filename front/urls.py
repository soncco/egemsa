from django.conf.urls import url

from . import views

app_name = 'front'
urlpatterns = [

    url(r'^$', views.index, name = 'index'),
    url(r'^categoria/(?P<slug>[-\w]+)/$', views.categoria, name = 'categoria'),
    url(r'^actividades-oficiales/$', views.actividades, name = 'actividades'),
    url(r'^documento/(?P<id>.*)$', views.documento, name = 'documento'),
    url(r'^agenda/(?P<id>.*)$', views.agenda, name = 'agenda'),
    url(r'^evento/(?P<id>.*)$', views.evento, name = 'evento'),
    url(r'^buscar/$', views.buscar, name = 'buscar'),
]
