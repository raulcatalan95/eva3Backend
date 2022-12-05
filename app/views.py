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
    #AppAdministracion_Usuarios.objects.create('admin', 'adminadmin','a@admin.cl','administrador general',0)
    #AppAdministracion_Usuarios.objects.create(username = 'admin1', password= 'adminadmin1', email= 'a@admin.clq',nombre='administrador oficina',perfil=1)
    #AppAdministracion_Usuarios.objects.create(username = 'admin2', password= 'adminadmin2', email= 'a@adminn.clq',nombre='administrador computacion',perfil=3)
    #AppAdministracion_Usuarios.objects.create(username = 'admin3', password= 'adminadmin3', email= 'a@adminnn.clq',nombre='administrador vehiculos',perfil=2)
    sesion = None
    try:
        sesion = request.session['sesion_activa']
        if sesion == 0:
            #sesion = None
            return redirect(adminGeneral)
        elif sesion == 1:
            #sesion = None
            return redirect(adminOficina)
        elif sesion == 3:
            #sesion = None
            return redirect(adminComputacion)
        elif sesion == 2:
            #sesion = None
            return redirect(adminVehiculos)
        else:
            return render(request,"home.html",{'sesion_activa':sesion})
    except:
        sesion = None
        return render(request,"home.html",{'sesion_activa':sesion})

def adminGeneral(request):
    sesion = None
    try:
        sesion = request.session['sesion_activa']
        if sesion == 1:
            #sesion = None
            return redirect(adminOficina)
        elif sesion == 3:
            #sesion = None
            return redirect(adminComputacion)
        elif sesion == 2:
            #sesion = None
            return redirect(adminVehiculos)
        elif sesion == 0:
            #sesion = None
            return render(request,"admins/admin_general.html",{'sesion_activa':sesion})    
    except:
        sesion = None
        return render(request,"home.html",{'sesion_activa':sesion})

def adminOficina(request):
    sesion = None
    try:
        sesion = request.session['sesion_activa']
        if sesion == 3:
            #sesion = None
            return redirect(adminComputacion)
        elif sesion == 2:
            #sesion = None
            return redirect(adminVehiculos)
        elif sesion == 1:
            return render(request, 'admins/admin_oficina.html')
        elif sesion == 0:
            return render(request, 'admins/admin_oficina.html')
    except:
        sesion = None
        return render(request,"home.html",{'sesion_activa':sesion})
    

def adminComputacion(request):
    sesion = None
    try:
        sesion = request.session['sesion_activa']
        if sesion == 1:
            #sesion = None
            return redirect(adminOficina)
        elif sesion == 2:
            #sesion = None
            return redirect(adminVehiculos)
        elif sesion == 3:
            return render(request, 'admins/admin_computacion.html')
        elif sesion == 0:
            return render(request, 'admins/admin_computacion.html')
    except:
        sesion = None
        return render(request,"home.html",{'sesion_activa':sesion})
    

def adminVehiculos(request):
    sesion = None
    try:
        sesion = request.session['sesion_activa']
        if sesion == 1:
            #sesion = None
            return redirect(adminOficina)
        elif sesion == 3:
            #sesion = None
            return redirect(adminComputacion)
        elif sesion == 2:
            return render(request, 'admins/admin_vehiculos.html')
        elif sesion == 0:
            return render(request, 'admins/admin_vehiculos.html')
    except:
        sesion = None
        return render(request,"home.html",{'sesion_activa':sesion})
    

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

def login(request):
    try:
        if request.session['sesion_activa'] == 'Activa0':
            #del request.session['sesion_activa']
            return redirect(inicio)
        else:
            return render(request,"registration/login.html")
    except:
        return render(request,"registration/login.html")

def sesion(request):
    per = None
    try:
        per = AppAdministracion_Usuarios.objects.get(username = request.POST["user_name"])
        if(per.password == request.POST["contrasena"]):
            request.session["sesion_activa"] = per.perfil
            return redirect(inicio)
        else:
           return render(request,"registration/login.html", {"mensaje":"contraseña no válida"})
    except Exception as ex:
        return render(request,"registration/login.html", {"mensaje":ex})


    

