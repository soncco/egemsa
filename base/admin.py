# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from base.models import Categoria, Documento, Archivo

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ['nombre',]

class ArchivoInline(admin.TabularInline):
    model = Archivo

class DocumentoAdmin(admin.ModelAdmin):
    inlines = [ArchivoInline,]
    list_display = ('nombre', 'fecha', 'categoria', 'creado_por')
    search_fields = ['nombre']
    list_filter = ('fecha', 'categoria', 'creado_por')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Documento, DocumentoAdmin)



