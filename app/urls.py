"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.inicio),
    path('cuentas/',include('django.contrib.auth.urls')),
    path('home', views.home),
    path('ingresarArticulos', views.ingresarArticulos),
    path('listarArticulos', views.listarArticulos),
    path('eliminaArticulo', views.eliminaArticulo),
    path('eliminarArticulos', views.eliminarArticulos),
    path('actualizarArticulos', views.actualizarArticulos),
    path('ingresarVehiculo', views.ingresarVehiculo),
    path('registrarVehiculo', views.registrarVehiculo),
    path('registrarArticulos', views.registrarArticulos),
    path('editarArticulo', views.editarArticulo),
    path('actualizarVehiculo', views.actualizarVehiculo),
    path('editarVehiculo', views.editarVehiculo),
    path('filtroarticulo', views.filtroarticulo),
    path('eliminarVehiculo', views.eliminarVehiculo),
    path('eliminaVehiculo', views.eliminaVehiculo),
    path('listarVehiculo', views.listarVehiculo),
    path('filtroVehiculo', views.filtroVehiculo),
    path('ingresarComputacion', views.ingresarComputacion),
    path('filtroComputacion', views.filtroComputacion),
    path('listarComputacion', views.listarComputacion),
    path('registrarComputacion', views.registrarComputacion),
    path('editarComputacion', views.editarComputacion),
    path('actualizarComputacion', views.actualizarComputacion),
    path('eliminarComputacion', views.eliminarComputacion),
    path('eliminaComputacion', views.eliminaComputacion),
    path('eliminarUsuario', views.eliminarUsuario),
    path('eliminaUsuario', views.eliminaUsuario),
    path('ingresarUsuario', views.ingresarUsuario),
    path('registrarUsuario', views.registrarUsuario),
    path('listarUsuario', views.listarUsuario),
    path('actualizarUsuario', views.actualizarUsuario),
    path('editarUsuario', views.editarUsuario),
    path('registro', views.registro, name='registro'),
    path('logout',views.cerrar_sesion),

]