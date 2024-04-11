from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('start_encuesta', start_encuesta, name="start_encuesta"),

]
