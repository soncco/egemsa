# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

@python_2_unicode_compatible
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

@python_2_unicode_compatible
class Documento(models.Model):
    categoria = models.ForeignKey(Categoria)
    nombre = models.CharField(max_length=255)
    fecha = models.DateField()
    descripcion = RichTextField()
    creado_por = models.ForeignKey(User)

    def __str__(self):
        return self.nombre

@python_2_unicode_compatible
class Archivo(models.Model):
    pertenece_a = models.ForeignKey(Documento)
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='../static/archivos', max_length=255)

    def __str__(self):
        return self.nombre

@python_2_unicode_compatible
class Participante(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

@python_2_unicode_compatible
class Agenda(models.Model):
    dirige = models.ForeignKey(Participante)
    junto_con = models.TextField()
    fecha_hora = models.DateTimeField()
    asunto = models.TextField()
    lugar = models.CharField(max_length=255)
    creado_por = models.ForeignKey(User)

    def __str__(self):
        return self.asunto
