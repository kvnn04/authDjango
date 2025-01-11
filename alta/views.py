from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignUp
# from ..src.jwt.controller import ControllerJwt
from src.jwt.controller import ControllerJwt
from .models import Usuario
def saludo(request):
    return HttpResponse("¡Hola, bienvenido a mi sitio web!")

def register(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            # print(form) me muestra todo el html esto.
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('pwd')

            # encodeContrasenia = ControllerJwt().crearObjectEncode().encodeForInDb({'pwd': password})

            nuevoUsuario=Usuario(
                username=username,
                email=email,
            )
            nuevoUsuario.set_password(password)
            nuevoUsuario.save()

            return render(request, 'main.html')  # Redirigir o renderizar una página de éxito
    else:
        form = SignUp()

    return render(request, 'main.html', {'form': form})