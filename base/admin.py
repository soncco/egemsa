# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from base.models import Categoria, Documento, Archivo, Participante, Agenda

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('cadena',)
    search_fields = ['nombre',]
    list_filter = ('padre',)
    prepopulated_fields = {'slug': ('nombre',)}

class ArchivoInline(admin.TabularInline):
    model = Archivo

class DocumentoAdmin(admin.ModelAdmin):
    inlines = [ArchivoInline,]
    list_display = ('nombre', 'fecha', 'categoria', 'creado_por',)
    search_fields = ['nombre']
    list_filter = ('fecha', 'categoria', 'creado_por',)

class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ['nombre',]

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('dirige', 'fecha_hora', 'lugar', 'creado_por',)
    search_fields = ['dirige', 'asunto']
    list_filter = ('dirige', 'fecha_hora', 'lugar', 'creado_por',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Participante, ParticipanteAdmin)
admin.site.register(Agenda, AgendaAdmin)
