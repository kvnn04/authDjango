from django.urls import path
from .views import bajaUsuario
urlpatterns = [
    path('delete/', view=bajaUsuario, name='deleteUsuario'),
    # path('login/', view=login_view, name='login')
]