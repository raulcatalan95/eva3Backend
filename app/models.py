from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser


class AppAdministracion_Vehiculos(models.Model):
    patente =  models.CharField(primary_key = True, max_length=6),
	numero_chasis = models.CharField(unique=True, null=False),

