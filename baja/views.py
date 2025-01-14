from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def bajaUsuario(request):
    try:
        print(request)
        print(request.user)
        print(request.user.id)
        print(request.user.username)
        print(request.user.email)
        print('El usuario esta autenticado?',request.user.is_authenticated)
        print('El usuario tiene permiso de administrador?',request.user.is_staff)
        print('Es superUsuario?',request.user.is_superuser)
        if request.user.is_authenticated:
            usuario = request.user
            logout(request)
            usuario.delete()
        return HttpResponse('Fue eliminado correctamente')
        
    except Exception:
        return HttpResponse('Debe iniciar sesion para darse de baja')


    