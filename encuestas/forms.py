from django.db import models
from django.forms import ModelForm
from encuestas.models import *


class CreateEncuestaForm(ModelForm):
    class Meta:
        model = Encuesta
        fields = '__all__'
