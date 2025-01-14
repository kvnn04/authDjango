from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm

# Create your views here.

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)

#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')

#         user = authenticate(request, username=username, password=password)
#         print(user)
#         if user is not None:
#             login(request, user)
#             print(user, 'adfafd')
#             return redirect('signup')  # Redirige a la página principal o cualquier otra
#         else:
#             messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
#     return render(request, 'login.html', {'form': LoginForm()})


def bajaUsuario(request, id: int):
    # usuario = Usuario.objects.filter(id=id).first() # Esto me trae el usuario y si no lo encuentra devuelve none
    try: 
        usuarios = Usuario.objects.get(id=id) # esto va a traer el usuario y si no lo encuentra tira una excepcion
        print(usuarios) # id aparece aunque yo no lo haya agregado
        print(request)
        perteneciaUsuario = usuarios.id == id
        
        if not perteneciaUsuario:
            return JsonResponse(data={'error': 'No tenes acceso'}, status=403)
        
        return render(request=request, template_name='index.html', context={'usuarios': usuarios})
    except Usuario.DoesNotExist:
        return JsonResponse(data={'error': 'No found'}, status=403)
        # return JsonResponse



    