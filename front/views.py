# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404

from base.models import Categoria, Documento, Agenda, Participante
from .utils import fechas

from datetime import datetime


def index(request):
    categorias = Categoria.objects.all()
    documentos = Documento.objects.all().order_by('-id')[:10]
    agendas = Agenda.hoy.eventos_hoy()
    
    context = {'categorias': categorias, 'documentos': documentos, 'agendas': agendas}
    return render(request, 'front/index.html', context)


def categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    documentos = Documento.objects.filter(categoria = categoria)
    categorias = Categoria.objects.filter(~Q(pk = categoria.pk))

    page = request.GET.get('page', 1)
    paginator = Paginator(documentos, 10)

    try:
        documentos = paginator.page(page)
    except PageNotAnInteger:
        documentos = paginator.page(1)
    except EmptyPage:
        documentos = paginator.page(paginator.num_pages)

    context = {'categorias': categorias, 'categoria': categoria, 'documentos': documentos}
    return render(request, 'front/categoria.html', context)


def documento(request, id):
    documento = get_object_or_404(Documento, pk = id)

    documentos = Documento.objects.filter(categoria = documento.categoria)
    documentos = documentos.filter(~Q(pk = documento.pk))[:5]

    context = {'documento': documento, 'documentos': documentos}
    return render(request, 'front/documento.html', context)


def actividades(request):
    participantes = Participante.objects.all()
    participante = participantes[:1][0]
    
    return agenda(request, participante.id)


def agenda(request, id):
    participante = get_object_or_404(Participante, pk=id)
    categorias = Categoria.objects.all()
    participantes = Participante.objects.all()

    today = datetime.now().date()

    fecha = request.GET.get('fecha')
    if fecha is not None:
        fecha, fecha_end, fecha_start = fechas(fecha)
        agendas = Agenda.objects.filter(dirige = participante, fecha_hora__lte=fecha_end, fecha_hora__gte=fecha_start).order_by('fecha_hora')
    else:
        fecha = today
        agendas = Agenda.hoy.eventos_hoy().filter(dirige = participante)

    context = {'categorias': categorias, 'agendas': agendas, 'fecha': fecha, 'participantes': participantes, 'actual': participante}
    return render(request, 'front/agenda.html', context)

def evento(request, id):
    evento = get_object_or_404(Agenda, pk = id)