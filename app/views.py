from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from .models import AppAdministracion_InsumosOficina
from .models import AppAdministracion_Vehiculos
from .models import AppAdministracion_InsumosComputacionales
from .models import AppAdministracion_Usuarios

def inicio(request):
    return render(request, 'home.html')

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            nombre_usuario = formulario.cleaned_data['username']
            contrasenna = formulario.cleaned_data['password1']
            usu = authenticate(username=nombre_usuario, password = contrasenna)
            login(request, usu)
            return redirect(inicio)
    else:
        formulario = UserCreationForm()
    contexto = {'form' : formulario}
    return render(request, 'registration/registro.html', context=contexto)

def cerrar_sesion(request):
    logout(request)
    return redirect(inicio)

def ingresarArticulos(request):
    id_activo_automatic = AppAdministracion_InsumosOficina.objects.all().count() + 1
    idco = id_activo_automatic
    return render(request,"adminOficina/ingresarArticulos.html",{'idco':idco})

def home(request):
    return render(request,"home.html")

def registrarArticulos(request):
    mensaje = "Articulo ingresado correctamente"
    nro_arti = request.POST['nro_articulo']
    nombre_arti= request.POST['nombre']
    ubicacion_arti = request.POST['ubicacion']
    stock_arti = request.POST['stock']
    descripcion_arti = request.POST['descripcion']
    AppAdministracion_InsumosOficina.objects.create(nro_articulo = nro_arti,nombre = nombre_arti, ubicacion = ubicacion_arti,stock=stock_arti, descripcion = descripcion_arti)
    return render(request, 'respuestaHtas.html',{"mensaje": mensaje})


    

