from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser


class AppAdministracion_Vehiculos(models.Model):
    patente =  models.CharField(primary_key = True, max_length=6)
    numero_chasis = models.CharField(unique=True, null=False, max_length=17)
    marca = models.CharField(null=False, max_length=20)
    modelo= models.CharField(null=False, max_length=10)
    ultima_revision= models.DateField(null=False)
    proxima_revision= models.DateField(null=False)
    observaciones= models.CharField(max_length=200)


class AppAdministracion_InsumosComputacionales(models.Model):

    numero_insumo = models.IntegerField(primary_key=True)
    nombre = models.CharField(null=False, max_length=20)
    fecha_adquisicion = models.DateField(null=False)
    marca = models.CharField(max_length =30)
    stock = models.IntegerField(null=False)
    descripcion = models.CharField(max_length =100)

class AppAdministracion_InsumosOficina(models.Model):
    nro_articulo = models.IntegerField(primary_key=True)
    nombre = models.CharField(null=False, max_length=50)
    ubicacion = models.CharField(null=False, max_length=25)
    stock = models.IntegerField(null=False)
    descripcion = models.CharField(max_length =100)


class AppAdministracion_Usuarios(models.Model):
    username = models.CharField(primary_key=True, max_length=25)
    password = models.CharField(unique=True, max_length=40)
    email = models.CharField(null=False, max_length=60)
    nombre = models.CharField(null=False, max_length=60)
    perfil = models.IntegerField(null=False)


##insert into AppAdministracion_Usuarios values('admin', 'adminadmin','a@admin.cl','administrador general',0)



