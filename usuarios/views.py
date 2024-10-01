from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .models import Profile


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse nome.')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        profile = Profile.objects.create(user=user, telefone=telefone)
        profile.save()

        return HttpResponse('Usuário cadastrado com sucesso!')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)

            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Email ou senha inválido')
        
@login_required(login_url="/auth/login")
def plataforma(request):
    return HttpResponse('Só tem acesso a essa parte logado')
