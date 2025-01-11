from django.db import models
from django.db.models import CharField
from django.contrib.auth.hashers import make_password
# Create your models here.

class Usuario(models.Model):
    # nombre: CharField = CharField(max_length=70)
    # apellido: CharField = CharField(max_length=70)
    username: CharField = CharField(max_length=150, null=False, blank=False, unique=True)
    email: CharField = CharField(max_length=150, null=False, blank=False, unique=True)
    pwd: CharField = CharField(max_length=70, null=False, blank=False)

    def __rerp__(self):
        return self.username
    
    def set_password(self, raw_password):
        """Hashea la contraseña antes de almacenarla"""
        self.pwd = make_password(raw_password)

    def check_password(self, raw_password):
        """Verifica si la contraseña proporcionada coincide con el hash almacenado"""
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.pwd)
