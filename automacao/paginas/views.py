from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def cadastro_usuario(request):
    if request.method == "GET":
        return render(request, 'paginas/cadastro.html')
    else:
        username= request.POST.get('username')
        email= request.POST.get('email')
        senha= request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Já existe um usuário com este nome')
        else:
            usuario = User.objects.create_user(username=username,email=email,password=senha)
            usuario.save()
            return HttpResponse("Usuario cadastrado")



def login_usuario(request):
    if request.method == 'GET':
        return render(request, 'paginas/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,'Usuario ou senha invalida!!!')
            return redirect('/')


@login_required(login_url='/')
def home(request):
    if request.user.is_authenticated:
        return HttpResponse('plataforma')
