# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from base.models import Categoria, Documento, Agenda, Participante
from .utils import fechas, get_fecha

from datetime import datetime



def index(request):
    categorias = cache.get('categorias:padres')
    if categorias is None:
        categorias = Categoria.padres.all()
        cache.set('categorias:padres', categorias)

    documentos = cache.get('documentos:ultimos')
    if documentos is None:
        documentos = Documento.objects.all().order_by('-id')[:10]
        cache.set('documentos:ultimos', documentos)

    agendas = Agenda.hoy.eventos_hoy()
    
    context = {'categorias': categorias, 'documentos': documentos, 'agendas': agendas}
    return render(request, 'front/index.html', context)


def categoria(request, slug):
    categoria = cache.get('categorias:slug:%s' % slug)
    if categoria is None:
        categoria = get_object_or_404(Categoria, slug=slug)
        cache.get('categorias:slug:%s' % slug, categoria)

    categorias = cache.get('categorias:padres')
    if categorias is None:
        categorias = Categoria.padres.all()
        cache.set('categorias:padres', categorias)

    context = {'categorias': categorias, 'categoria': categoria}
    return render(request, 'front/categoria.html', context)


def documento(request, id):
    documento = cache.get('documentos:pk:%s' % str(id))
    if documento is None:
        documento = get_object_or_404(Documento, pk = id)
        cache.set('documentos:pk:%s' % str(id), documento)

    documentos = cache.get('documentos:categoria:%d' % documento.categoria.pk)
    if documentos is None:
        documentos = Documento.objects.filter(categoria = documento.categoria)
        documentos = documentos.filter(~Q(pk = documento.pk))[:5]
        cache.set('documentos:categoria:%d' % documento.categoria.pk, documentos)

    context = {'documento': documento, 'documentos': documentos}
    return render(request, 'front/documento.html', context)


def actividades(request):
    participantes = Participante.objects.all()
    participante = participantes[:1][0]
    
    return agenda(request, participante.id)


def agenda(request, id):
    participante = get_object_or_404(Participante, pk=id)

    categorias = cache.get('categorias:padres')
    if categorias is None:
        categorias = Categoria.padres.all()
        cache.set('categorias:padres', categorias)

    participantes = Participante.objects.all()

    today = datetime.now().date()

    fecha = request.GET.get('fecha')
    if fecha is not None:
        fecha, fecha_end, fecha_start = fechas(fecha)
        agendas = Agenda.objects.filter(Q(dirige = participante) | Q(participan = participante), fecha_hora__lte=fecha_end, fecha_hora__gte=fecha_start).order_by('fecha_hora')
    else:
        fecha = today
        agendas = Agenda.hoy.eventos_hoy().filter(Q(dirige = participante) | Q(participan = participante))

    context = {'categorias': categorias, 'agendas': agendas, 'fecha': fecha, 'participantes': participantes, 'actual': participante}
    return render(request, 'front/agenda.html', context)

def evento(request, id):
    evento = get_object_or_404(Agenda, pk = id)
    context = {'evento': evento}
    return render(request, 'front/evento.html', context)

def buscar(request):
    q = request.GET.get('q', '')
    first = request.GET.get('first')
    categorias = Categoria.padres.all()
    documentos = Documento.objects.filter(Q(nombre__icontains = q) | Q(nombre__icontains = q))

    if first != '':
        cats = request.GET.getlist('categoria[]')
        if len(cats) > 0:
            documentos = documentos.filter(Q(categoria__padre__padre__padre__pk__in = cats) | Q(categoria__padre__padre__pk__in = cats) | Q(categoria__padre__pk__in = cats) | Q(categoria__pk__in = cats))

        desde = request.GET.get('desde')
        hasta = request.GET.get('hasta')
        if hasta == '' and desde != '':
            desde = get_fecha(desde)
            documentos = documentos.filter(fecha__gte = desde)
        elif hasta != '' and desde != '':
            desde = get_fecha(desde)
            hasta = get_fecha(hasta)
            documentos = documentos.filter(fecha__range = (desde, hasta))
        else:
            desde = None
            hasta = None


    page = request.GET.get('page', 1)
    paginator = Paginator(documentos, 10)

    try:
        documentos = paginator.page(page)
    except PageNotAnInteger:
        documentos = paginator.page(1)
    except EmptyPage:
        documentos = paginator.page(paginator.num_pages)

    if first != '':
        cats = [ int(x) for x in cats ]    
        context = {'categorias': categorias, 'documentos': documentos, 'cats': cats, 'desde': desde, 'hasta': hasta}
    else:
        context = {'categorias': categorias, 'documentos': documentos}

    return render(request, 'front/buscar.html', context)

def handler404(request):
    response = render(request, 'front/404.html', {})
    response.status_code = 403
    return response

def handler403(request):
    response = render(request, 'front/403.html', {})
    response.status_code = 403
    return response

import sys
def handler500(request):
    type_, value, traceback = sys.exc_info()
    response = render(request, 'front/500.html', {'value_': value})
    response.status_code = 500
    return response
