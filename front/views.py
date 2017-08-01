# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from base.models import Categoria, Documento

def index(request):
    categorias = Categoria.objects.all()
    documentos = Documento.objects.all().order_by('-id')[:10]
    context = {'categorias': categorias, 'documentos': documentos}
    return render(request, 'front/index.html', context)