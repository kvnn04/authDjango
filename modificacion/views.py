from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ModifyNombreApellido

# Create your views here.
# @login_required
# def modificarUsuario(request):
#     message = f'el usuario {request.user.email} fue modificado'
#     return HttpResponse(message)
@login_required
def modificarUsuarioNameAndApellido(request):
    if request.method == 'POST':
        userInDb = get_object_or_404(User, id=request.user.id)

        # Obtener datos del formulario (por ejemplo, request.POST)
        newNombre = request.POST.get('nombre', userInDb.last_name)
        newApellido = request.POST.get('apellido', userInDb.first_name)
        
        userInDb.first_name = newNombre
        userInDb.last_name = newApellido
        return HttpResponse('Usuario modificado con exito')

    return render(request=request, template_name='modifyNameApellido.html',context={'form': ModifyNombreApellido()})