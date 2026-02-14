from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(
        max_length=70
        )
    apellido = models.CharField(
        max_length=70
        )
    edad = models.IntegerField()
    email = models.EmailField()
    sexo = models.CharField(max_length=1)
    telefono = models.CharField(max_length=10, default="")


class Contacto(models.Model):
    nombre = models.CharField(max_length=70)
    email = models.EmailField()
    mensaje = models.TextField()
    
    