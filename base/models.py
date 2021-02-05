from django.db import models
from django.contrib.auth.models import User

from datetime import datetime, timedelta, time

from ckeditor.fields import RichTextField

class CategoriaManager(models.Manager):
    def all(self):
        return self.filter(padre = None)

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    padre = models.ForeignKey('Categoria', blank=True, null=True, on_delete=models.DO_NOTHING)

    def cadena(self):
        if self.padre is None:
            return self.nombre
        else:
            return self.padre.cadena() + ' > ' + self.nombre

    def __str__(self):
        return self.cadena()

    objects = models.Manager()
    padres = CategoriaManager()


class Documento(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=255)
    fecha = models.DateField()
    descripcion = RichTextField(null=True, blank=True)
    enlace = models.URLField(max_length=255, blank=True, null=True)
    creado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    orden_anual = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Archivo(models.Model):
    fecha = models.DateField()
    pertenece_a = models.ForeignKey(Documento, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='', max_length=255)

    def ext(self):
        return self.archivo.url.split('.')[-1]

    def extension(self):
        ext = self.ext()
        if ext == 'doc' or ext == 'docx':
            return 'fa-file-word-o text-info'
        elif ext == 'xls' or ext == 'xlsx':
            return 'fa-file-excel-o text-success'
        elif ext == 'pdf':
            return 'fa-file-pdf-o text-danger'
        else:
            return 'fa-file-o text-warning'

    def __str__(self):
        return self.nombre

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
        agendas = self.filter(fecha_hora__lte=today_end, fecha_hora__gte=today_start).order_by('fecha_hora')
        return agendas


class Agenda(models.Model):
    asunto = models.CharField(max_length=255)
    dirige = models.ForeignKey(Participante, related_name='Dirige', on_delete=models.PROTECT)
    participan = models.ManyToManyField(Participante, related_name='Participan', blank=True)
    junto_con = models.TextField(null=True, blank=True)
    fecha_hora = models.DateTimeField()
    lugar = models.CharField(max_length=255, blank=True, null=True)
    descripcion = RichTextField(null=True, blank=True)
    creado_por = models.ForeignKey(User, on_delete=models.PROTECT)

    objects = models.Manager()
    hoy = AgendaManager()

    def __str__(self):
        return self.asunto
