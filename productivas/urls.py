from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('Comenzar_Encuesta', start_encuesta_productiva, name="start_encuesta_productiva"),
    path('crearPreguntasProductiva', crearPreguntasProductiva, name="crearPreguntasProductiva"),

]
