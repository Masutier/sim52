from django.shortcuts import render
from .forms import CreateEncuestaForm


def encuestas(request):

    context = {"title":"Encuestas"}
    return render(request, 'encuestas/encuestas.html', context)


def create_encuesta(request):

    #CREAR ENCUESTA
    form = CreateEncuestaForm()

    if request.method == "POST":
        encuesta = request.POST

        print(encuesta)
        print(encuesta['pregunta'])
        


    #CREAR PREGUNTAS


    #GUARDAR EN DB


    context = {"title":"Crear Encuestas", "form":form}
    return render(request, 'encuestas/crearEncuesta.html', context)
