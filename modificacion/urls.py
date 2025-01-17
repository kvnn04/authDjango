from django.urls import path
from .views import modificarUsuarioNameAndApellido
urlpatterns = [
    path('user/', view=modificarUsuarioNameAndApellido, name='modificarUsuario'),
]