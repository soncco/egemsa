from django.urls import path

from front import views

app_name = 'front'
urlpatterns = [

    path('', views.index, name = 'index'),
    path('categoria/<slug:slug>/', views.categoria, name = 'categoria'),
    path('actividades-oficiales/', views.actividades, name = 'actividades'),
    path('documento/<int:id>', views.documento, name = 'documento'),
    path('agenda/<int:id>', views.agenda, name = 'agenda'),
    path('evento/<int:id>', views.evento, name = 'evento'),
    path('buscar/', views.buscar, name = 'buscar'),
]
