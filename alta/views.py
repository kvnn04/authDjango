from django.shortcuts import redirect, render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignUp, Login
# from ..src.jwt.controller import ControllerJwt
from src.jwt.controller import ControllerJwt
from .models import Usuario
# from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

def saludo(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('pwd')

            # Comprobamos si el usuario o el email ya existen en la base de datos
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Este nombre de usuario ya está en uso')
            elif User.objects.filter(email=email).exists():
                form.add_error('email', 'Este email ya está en uso')
            else:
                try:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    login(request, user)  # Asegúrate de pasar el 'request' y el 'user' correctamente
                    return redirect('logIn')  # Redirigimos a la página de login después de crear al usuario
                except Exception as e:
                    print(e)
                    return render(request, 'main.html', {'form': form, 'error': 'Ocurrió un error inesperado al crear el usuario.'})
        else:
            # Si el formulario no es válido, renderizamos con los errores
            return render(request, 'main.html', {'form': form})

    # Si no es un POST, solo mostramos el formulario vacío
    form = SignUp()
    return render(request, 'main.html', {'form': form})

def logIn(request):
    if request.method == 'GET':
            # Presenta el formulario vacío al usuario
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form})

    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        # Validamos el formulario y autenticamos al usuario
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Iniciamos sesión y redirigimos
                login(request, user)
                return redirect('home')  # Cambia 'home' por la vista donde deseas redirigir al usuario
            else:
                # Si la autenticación falla, mostramos el formulario con un mensaje de error
                return render(request, 'login.html', {'form': form, 'error': 'Credenciales inválidas'})

        # Si el formulario no es válido, mostramos los errores
        return render(request, 'login.html', {'form': form})
    
def logOut(request):
    logout(request)
    return redirect('home')