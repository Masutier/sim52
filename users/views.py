from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user
from .forms import EnterForm, UserRegisterForm


def profile(request):

    context={"title":"Sim52-Users"}
    return render(request, "users/profile.html", context)


@unauthenticated_user
def enter(request):
    form = EnterForm()
    
    if request.method == 'POST':
        form = EnterForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, f'Algo no salio bien, Intentalo de nuevo')

    context = {'title':'Enter', 'form':form}
    return render(request, 'users/enter.html', context)


def userLogout(request):
    logout(request)
    return redirect('home')


@unauthenticated_user
def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            group = Group.objects.get(name='user_rol')
            user.groups.add(group)
            login(request, user)
            messages.success(request, f'El usuario se creo satisfactoriamente')
            return redirect("profile")
        else:
            messages.info(request, f'Algo no salio bien, Intentalo de nuevo')
            return redirect("home")

    context = {'title':'Registro de Usuario', 'form':form}
    return render(request, 'users/register.html', context)

