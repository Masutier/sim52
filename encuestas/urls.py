from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('encuestas', encuestas, name="encuestas"),
    path('create_encuesta', create_encuesta, name="create_encuesta"),

]
