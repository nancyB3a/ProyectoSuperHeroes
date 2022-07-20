from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Compagnia(models.Model):
    idCompagnia=models.IntegerField(primary_key=True, verbose_name="Id de Compañia")
    nombreCompagnia= models.CharField(max_length=15, verbose_name="Nombre Compañia")

    def __str__(self):
        return self.nombreCompagnia

class Personaje(models.Model):
    idPersonaje=models.AutoField(primary_key=True, verbose_name="Id Personaje")
    nombre=models.CharField(max_length=20, verbose_name="Nombre")
    descripcion=models.CharField(max_length=200, verbose_name="Descripcion")
    team=models.CharField(max_length=12, verbose_name="Team")
    foto=models.ImageField(upload_to='personajes', null=True)
    compagnia=models.ForeignKey(Compagnia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre