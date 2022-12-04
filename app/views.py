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


def actualizarArticulos(request):
    return render(request, 'adminOficina/actualizarArticulos.html')


def editarArticulo(request):
    arti = None
    mensaje = ""
    try:
        arti = AppAdministracion_InsumosOficina.objects.get(nro_articulo = request.GET["nro_articulo"])
        return render(request, "adminOficina/actualizarArticulos.html", {"artic":arti,})
    except:
        arti = None
    
    if arti == None:
        nro_articulo = None
        try:
            nro_articulo = request.POST["nro_articulo"]
        except:
            nro_articulo = None

        if nro_articulo != None:
            arti = AppAdministracion_InsumosOficina.objects.get(nro_articulo = nro_articulo)

            nro_articulo_a = request.POST["nro_articulo"]
            nombre_a = request.POST["nombre"]
            ubicacion_a = request.POST["ubicacion"]
            stock_a = request.POST["stock"]
            descripcion_a = request.POST["descripcion"]
            arti.nro_articulo = nro_articulo_a
            arti.nombre = nombre_a
            arti.ubicacion = ubicacion_a
            arti.stock = stock_a
            arti.descripcion = descripcion_a
            

            try:
                arti.save()
                mensaje = "Articulo actualizado con exito"
            except:
                mensaje = "Ha ocurrido un error al actualizar el Articulo"


            return render(request, "adminOficina/actualizarArticulos.html", {"mensaje":mensaje})
        
        else:
            mensaje = "No se ha encontrado el Articulo ingresado"

            return render(request, "adminOficina/actualizarArticulos.html", {"mensaje":mensaje})
    else:
        mensaje = "No se encontró el Articulo ingresado"

        return render(request, "adminOficina/actualizarArticulos.html", {"mensaje":mensaje})

    pass


    

