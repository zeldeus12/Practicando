from django.db import models

class Autores (models.Model):
    Nombre = models.CharField(max_length=50)

class Cancion (models.Model):
    Nombre = models.CharField(max_length=50)
    Genero  = models.CharField(max_length=50)
    Lanzamiento = models.DateTimeField()

class AutorCancion (models.Model):
    NombreC = models.ForeignKey(Cancion,on_delete=models.CASCADE)
    NombreA = models.ForeignKey(Autores,on_delete=models.CASCADE)

    def __init__(self):

        return self
# Create your models here.
