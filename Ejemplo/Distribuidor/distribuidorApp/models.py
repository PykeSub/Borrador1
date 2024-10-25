from django.db import models

# Create your models here.
class Distribuidores(models.Model):
    telefono = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    fechaDespacho = models.DateField(max_length=15)
    fechaRecepcion = models.DateField(max_length=15)
    ciudad = models.CharField(max_length=50)