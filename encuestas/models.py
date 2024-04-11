from django.db import models
from django.urls import reverse
from .models import *


class Encuesta(models.Model):
    encuestaname = models.CharField(max_length=60, null=True, blank=True)
    numpreguntas = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    def __str__(self):
        return self.encuestaname

