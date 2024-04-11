from django.shortcuts import render
from .forms import CreateEncuestaForm


def start_encuesta(request):

    #CREAR ENCUESTA
    form = CreateEncuestaForm()

    if request.method == "POST":
        encuestaname = request.POST.get('encuestaname')
        numeroPreguntas = request.POST.get('numpreguntas')

        context = {'title':"Crear Preguntas", 'encuestaname':encuestaname, 'numeroPreguntas':numeroPreguntas}
        return render(request, 'encuestas/crearPreguntas.html', context)
    

    #CREAR PREGUNTAS


    #GUARDAR EN DB


    context = {"title":"Crear Encuestas", "form":form}
    return render(request, 'encuestas/start_encuesta.html', context)
