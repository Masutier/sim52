from django.shortcuts import render, redirect
from .forms import CreateEncuestaProductivaForm, PreguntaProductiva


def start_encuesta_productiva(request):

    #CREAR ENCUESTA
    form = CreateEncuestaProductivaForm()

    if request.method == "POST":
        encuestaname = request.POST.get('encuestaname')
        numeroPreguntas = request.POST.get('numpreguntas')
        form1 = PreguntaProductiva()


        context = {'title':"Crear Preguntas", 'encuestaname':encuestaname, 'numeroPreguntas':numeroPreguntas, 'form1':form1}
        return render(request, 'productivas/crearPreguntasProductiva.html', context)

    #CREAR PREGUNTAS

    #GUARDAR EN DB

    context = {"title":"Comenzar Encuesta", "form":form}
    return render(request, 'productivas/start_encuesta_productiva.html', context)


def crearPreguntasProductiva(request):

    if request.method == "POST":
        enn = ('encuestaname')
        q1 = request.POST.get('question1')
        pre1 = request.POST.get('quest1')
        op1 = request.POST.get('opcion1a')
        op2 = request.POST.get('opcion2a')
        op3 = request.POST.get('opcion3a')
        op4 = request.POST.get('opcion4a')
        op5 = request.POST.get('opcion5a')
        
        print(enn)
        print(q1)
        print(pre1)
        print(op1)
        print(op2)
        print(op3)
        print(op4)
        print(op5)


    return redirect("/")