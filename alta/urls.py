from django.urls import path
from . import views

urlpatterns = [
    # path('', view=views.saludo, name='home'),
    path('signup/', view=views.register, name='signup'),
    path('login/', view=views.logIn, name='logIn'),
    path('logout/', view=views.logOut, name='logOut')
]