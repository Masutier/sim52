from django.contrib import messages
from django.shortcuts import render, redirect


def home(request):

    context={"title":"Sim52"}
    return render(request, 'sim52/home.html', context)


def privacy(request):

    context={"title": "Privacidad"}
    return render(request, 'sim52/info/privacy.html', context)


def condiciones(request):

    context={"title": "Condiciones"}
    return render(request, 'sim52/info/conditions.html', context)


def haveasData(request):

    context={"title": "Haveas Data"}
    return render(request, 'sim52/info/haveas_data.html', context)


def page501(request):

    context={"title": "Privacidad"}
    return render(request, 'sim52/errors/501.html', context)
