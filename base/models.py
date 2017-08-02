# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

from datetime import datetime, timedelta, time

from ckeditor.fields import RichTextField

@python_2_unicode_compatible
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.nombre

@python_2_unicode_compatible
class Documento(models.Model):
    categoria = models.ForeignKey(Categoria)
    nombre = models.CharField(max_length=255)
    fecha = models.DateField()
    descripcion = RichTextField(null=True, blank=True)
    creado_por = models.ForeignKey(User)

    def __str__(self):
        return self.nombre

@python_2_unicode_compatible
class Archivo(models.Model):
    pertenece_a = models.ForeignKey(Documento)
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='./static/archivos', max_length=255)

    def __str__(self):
        return self.nombre

@python_2_unicode_compatible
class Participante(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

today = datetime.now().date()
tomorrow = today + timedelta(1)
today_start = datetime.combine(today, time())
today_end = datetime.combine(tomorrow, time())
class AgendaManager(models.Manager):
    def eventos_hoy(self):
        agendas = self.filter(fecha_hora__lte=today_end, fecha_hora__gte=today_start)
        return agendas


@python_2_unicode_compatible
class Agenda(models.Model):
    dirige = models.ForeignKey(Participante)
    junto_con = models.TextField()
    fecha_hora = models.DateTimeField()
    asunto = models.TextField()
    lugar = models.CharField(max_length=255, blank=True, null=True)
    creado_por = models.ForeignKey(User)

    objects = models.Manager()
    hoy = AgendaManager()

    def __str__(self):
        return self.asunto
