from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #Se sobreescribe el metodo de login y ahora se pedira el email
    #y no el username como se hace predeterminadamente
    #agregar estas lineas luego de crear el super usuario en django
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

