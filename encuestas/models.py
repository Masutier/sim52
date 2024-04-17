from django.db import models
from django.urls import reverse
from .models import *


class Encuesta(models.Model):
    nombreEncuesta = models.CharField(max_length=60, null=True, blank=True)
    temaEncuesta = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    pregunta = models.CharField(max_length=160, null=True, blank=True)
    tipoPregunta = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    opcion1 = models.CharField(max_length=60, null=True, blank=True)
    opcion2 = models.CharField(max_length=60, null=True, blank=True)
    opcion3 = models.CharField(max_length=60, null=True, blank=True)
    opcion4 = models.CharField(max_length=60, null=True, blank=True)
    opcion5 = models.CharField(max_length=60, null=True, blank=True)
    fechaLibera = models.DateTimeField(auto_now_add=True, blank=True)
    duracion = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fechaCreacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombreEncuesta

