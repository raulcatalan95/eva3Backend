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
    q = AppAdministracion_InsumosOficina.objects.filter(nro_articulo__iexact = id_activo_automatic)
    idco = id_activo_automatic
    if q.count() > 0:
        idco = id_activo_automatic + 1
    q = AppAdministracion_InsumosOficina.objects.filter(nro_articulo__iexact = idco)
    if q.count() > 0:
        idco = idco + 5
    q = AppAdministracion_InsumosOficina.objects.filter(nro_articulo__iexact = idco)
    if q.count() > 0:
        idco = idco * 2 + 3
    return render(request,"adminOficina/ingresarArticulos.html",{'idco':idco})

def home(request):
    return render(request,"home.html")

def registrarArticulos(request):
    mensaje = "Articulo Oficina ingresado correctamente"
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
                mensaje = "Articulo Oficina actualizado con exito"
            except:
                mensaje = "Ha ocurrido un error al actualizar el Articulo de Oficina"


            return render(request, "adminOficina/actualizarArticulos.html", {"mensaje":mensaje})
        
        else:
            mensaje = "No se ha encontrado el Articulo ingresado"

            return render(request, "adminOficina/actualizarArticulos.html", {"mensaje":mensaje})
    else:
        mensaje = "No se encontró el Articulo ingresado"

        return render(request, "adminOficina/actualizarArticulos.html", {"mensaje":mensaje})

def listarArticulos(request):

    z = AppAdministracion_InsumosOficina.objects.all()

    return render(request,"adminOficina/listarArticulos.html", {'articulos': z})

def filtroarticulo(request):
    if request.GET["nombre_artic"]:
        fullarticulo = request.GET["nombre_artic"] # Get nombre
        q = AppAdministracion_InsumosOficina.objects.filter(nombre__iexact = fullarticulo) #comparacion del nombre ingresado
        w=q.count() #Contador de resgistros para el cliente buscado
        return render(request, "adminOficina/listarArticulos.html", {"fullarticulo" : q,"query":fullarticulo, "contador": w})

    if request.GET["numero_artic"]:
        fullarticulo = request.GET["numero_artic"] # Get nombre
        q = AppAdministracion_InsumosOficina.objects.filter(nro_articulo__iexact = fullarticulo) #comparacion del nombre ingresado
        w=q.count() #Contador de resgistros para el cliente buscado
        return render(request, "adminOficina/listarArticulos.html", {"fullarticulo" : q,"query":fullarticulo, "contador": w})
  
    if request.GET["ubicacion_artic"]:
        fullarticulo = request.GET["ubicacion_artic"] # Get nombre
        q = AppAdministracion_InsumosOficina.objects.filter(ubicacion__iexact = fullarticulo) #comparacion del nombre ingresado
        w=q.count() #Contador de resgistros para el cliente buscado
        return render(request, "adminOficina/listarArticulos.html", {"fullarticulo" : q,"query":fullarticulo, "contador": w})

    else:
        mensaje = "NO se indico ningun parametro de busqueda"
        z = AppAdministracion_InsumosOficina.objects.all()
        return render(request,"adminOficina/listarArticulos.html",{"mensaje": mensaje,'articulos': z})
    
def eliminarArticulos(request):
    return render(request,"adminOficina/eliminarArticulos.html")

def eliminaArticulo(request):
    
    mensaje = None
    try:
        artic = AppAdministracion_InsumosOficina.objects.get( nro_articulo = request.POST["nro_artic"])
        artic.delete()
        mensaje = "Articulo eliminado"
        return render(request, "respuestaHtas.html",{"mensaje":mensaje})
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            mensaje = 'Articulo no existe'
            return render(request, "respuestaHtas.html",{"mensaje":mensaje})
        else:
            mensaje = 'Ha ocurrido un problema al tratar de eliminar el articulo'
        return render(request, "respuestaHtas.html",{"mensaje":mensaje})    


def ingresarVehiculo(request):

    return render(request,"adminVehiculos/ingresarVehiculo.html")
    
def registrarVehiculo(request):
    mensaje = "Vehiculo ingresado correctamente"
    patente_a = request.POST['patente']
    numero_chasis_a= request.POST['numero_chasis']
    marca_a = request.POST['marca']
    modelo_a = request.POST['modelo']
    ultima_revision_a = request.POST['ultima_revision']
    proxima_revision_a = request.POST['proxima_revision']
    observaciones_a = request.POST['observaciones']
    AppAdministracion_Vehiculos.objects.create(patente = patente_a,numero_chasis = numero_chasis_a, marca = marca_a,modelo=modelo_a, ultima_revision = ultima_revision_a,proxima_revision = proxima_revision_a,observaciones = observaciones_a)
    return render(request, 'respuestaHtas.html',{"mensaje": mensaje})


def actualizarVehiculo(request):
    return render(request, "adminVehiculos/actualizarVehiculo.html")

def editarVehiculo(request):
    vehicu = None
    mensaje = ""
    try:
        vehicu = AppAdministracion_Vehiculos.objects.get(patente = request.GET["patente"])
        return render(request, "adminVehiculos/actualizarVehiculo.html", {"vehic":vehicu})
    except:
        vehicu = None
    
    if vehicu == None:
        patente = None
        try:
            patente = request.POST["patente"]
        except:
            patente = None

        if patente != None:
            vehicu = AppAdministracion_Vehiculos.objects.get(patente = patente)

            patente_a = request.POST["patente"]
            numero_chasis_a = request.POST["numero_chasis"]
            marca_a = request.POST["marca"]
            modelo_a = request.POST["modelo"]
            ultima_revision_a = request.POST["ultima_revision"]
            proxima_revision_a = request.POST["proxima_revision"]
            observaciones_a = request.POST["observaciones"]
            vehicu.patente = patente_a
            vehicu.numero_chasis = numero_chasis_a
            vehicu.marca = marca_a
            vehicu.modelo = modelo_a
            vehicu.ultima_revision = ultima_revision_a
            vehicu.proxima_revision = proxima_revision_a
            vehicu.observaciones = observaciones_a
            try:
                vehicu.save()
                mensaje = "Vehiculo actualizado con exito"
            except:
                mensaje = "Ha ocurrido un error al actualizar el Vehiculo"


            return render(request, "adminVehiculos/actualizarVehiculo.html", {"mensaje":mensaje})
        
        else:
            mensaje = "No se ha encontrado el Vehiculo ingresado"

            return render(request, "adminVehiculos/actualizarVehiculo.html", {"mensaje":mensaje})
    else:
        mensaje = "No se encontró el Vehiculo ingresado"

        return render(request, "adminVehiculos/actualizarVehiculo.html", {"mensaje":mensaje})

def eliminarVehiculo(request):
    return render(request,"adminVehiculos/eliminarVehiculo.html")

def eliminaVehiculo(request):
    
    mensaje = None
    try:
        vehicu = AppAdministracion_Vehiculos.objects.get( patente = request.POST["patente"])
        vehicu.delete()
        mensaje = "Vehiculo eliminado"
        return render(request, "respuestaHtas.html",{"mensaje":mensaje})
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            mensaje = 'Vehiculo no existe'
            return render(request, "respuestaHtas.html",{"mensaje":mensaje})
        else:
            mensaje = 'Ha ocurrido un problema al tratar de eliminar el Vehiculo'
        return render(request, "respuestaHtas.html",{"mensaje":mensaje})  

def listarVehiculo(request):

    z = AppAdministracion_Vehiculos.objects.all()

    return render(request,"adminVehiculos/listarVehiculo.html", {'vehiculos': z})


def filtroVehiculo(request):
    if request.GET["patente"]:
        fullVehiculo = request.GET["patente"] # Get nombre
        q = AppAdministracion_Vehiculos.objects.filter(patente__iexact = fullVehiculo) #comparacion del nombre ingresado
        w=q.count() #Contador de resgistros para el cliente buscado
        return render(request, "adminVehiculos/listarVehiculo.html", {"fullVehiculo" : q,"query":fullVehiculo, "contador": w})

    if request.GET["numero_chasis"]:
        fullVehiculo = request.GET["numero_chasis"] # Get nombre
        q = AppAdministracion_Vehiculos.objects.filter(numero_chasis__iexact = fullVehiculo) #comparacion del nombre ingresado
        w=q.count() #Contador de resgistros para el cliente buscado
        return render(request, "adminVehiculos/listarVehiculo.html", {"fullVehiculo" : q,"query":fullVehiculo, "contador": w})

    if request.GET["marca"]:
        fullVehiculo = request.GET["marca"] # Get nombre
        q = AppAdministracion_Vehiculos.objects.filter(marca__iexact = fullVehiculo) #comparacion del nombre ingresado
        w=q.count() #Contador de resgistros para el cliente buscado
        return render(request, "adminVehiculos/listarVehiculo.html", {"fullVehiculo" : q,"query":fullVehiculo, "contador": w})

    if request.GET["modelo"]:
        fullVehiculo = request.GET["modelo"] # Get nombre
        q = AppAdministracion_Vehiculos.objects.filter(modelo__iexact = fullVehiculo) #comparacion del nombre ingresado
        w=q.count() #Contador de resgistros para el cliente buscado
        return render(request, "adminVehiculos/listarVehiculo.html", {"fullVehiculo" : q,"query":fullVehiculo, "contador": w})

    else:
        mensaje = "NO se indico ningun parametro de busqueda"
        z = AppAdministracion_Vehiculos.objects.all()
        return render(request,"adminVehiculos/listarVehiculo.html",{"mensaje": mensaje,'vehiculos': z})

def ingresarComputacion(request):
    id_activo_automatic = AppAdministracion_InsumosComputacionales.objects.all().count() + 1
    q = AppAdministracion_InsumosComputacionales.objects.filter(numero_insumo__iexact = id_activo_automatic)
    idco = id_activo_automatic
    if q.count() > 0:
        idco = id_activo_automatic + 1
    q = AppAdministracion_InsumosComputacionales.objects.filter(numero_insumo__iexact = idco)
    if q.count() > 0:
        idco = idco + 5
    q = AppAdministracion_InsumosComputacionales.objects.filter(numero_insumo__iexact = idco)
    if q.count() > 0:
        idco = idco * 2 + 3
    return render(request,"adminComputacion/ingresarComputacion.html",{'idco':idco})

def registrarComputacion(request):
    mensaje = "Articulo de Computacion ingresado correctamente"
    numero_insumo_a = request.POST['numero_insumo']
    nombre_a= request.POST['nombre']
    fecha_adquisicion_a = request.POST['fecha_adquisicion']
    marca_a = request.POST['marca']
    stock_a = request.POST['stock']
    descripcion_a = request.POST['descripcion']
    AppAdministracion_InsumosComputacionales.objects.create(numero_insumo = numero_insumo_a,nombre = nombre_a, fecha_adquisicion = fecha_adquisicion_a,marca=marca_a, stock = stock_a,descripcion = descripcion_a)
    return render(request, 'respuestaHtas.html',{"mensaje": mensaje})

def listarComputacion(request):

    z = AppAdministracion_InsumosComputacionales.objects.all()

    return render(request,"adminComputacion/listarComputacion.html", {'computacion': z})

def filtroComputacion(request):
    if request.GET["numero_insumo"]:
        fullcomputacion = request.GET["numero_insumo"] # Get nombre
        q = AppAdministracion_InsumosComputacionales.objects.filter(numero_insumo__iexact = fullcomputacion) #comparacion del nombre ingresado
        w=q.count() #Contador de resgistros para el cliente buscado
        return render(request, "adminComputacion/listarComputacion.html", {"fullcomputacion" : q,"query":fullcomputacion, "contador": w})

    if request.GET["nombre"]:
        fullcomputacion = request.GET["nombre"] # Get nombre
        q = AppAdministracion_InsumosComputacionales.objects.filter(nombre__iexact = fullcomputacion) #comparacion del nombre ingresado
        w=q.count() #Contador de resgistros para el cliente buscado
        return render(request, "adminComputacion/listarComputacion.html", {"fullcomputacion" : q,"query":fullcomputacion, "contador": w})

    else:
        mensaje = "NO se indico ningun parametro de busqueda"
        z = AppAdministracion_InsumosOficina.objects.all()
        return render(request,"adminOficina/listarArticulos.html",{"mensaje": mensaje,'articulos': z})


def actualizarComputacion(request):
    return render(request, 'adminComputacion/actualizarComputacion.html')


def editarComputacion(request):
    comput = None
    mensaje = ""
    try:
        comput = AppAdministracion_InsumosComputacionales.objects.get(numero_insumo = request.GET["numero_insumo"])
        return render(request, "adminComputacion/actualizarComputacion.html", {"compu":comput})
    except:
        comput = None
    
    if comput == None:
        numero_insumo = None
        try:
            numero_insumo = request.POST["numero_insumo"]
        except:
            numero_insumo = None

        if numero_insumo != None:
            comput = AppAdministracion_InsumosComputacionales.objects.get(numero_insumo = numero_insumo)

            numero_insumo_a = request.POST["numero_insumo"]
            nombre_a = request.POST["nombre"]
            fecha_adquisicion_a = request.POST["fecha_adquisicion"]
            marca_a = request.POST["marca"]
            stock_a = request.POST["stock"]
            descripcion_a = request.POST["descripcion"]
            comput.numero_insumo = numero_insumo_a
            comput.nombre = nombre_a
            comput.fecha_adquisicion = fecha_adquisicion_a
            comput.marca = marca_a
            comput.stock = stock_a
            comput.descripcion = descripcion_a
            

            try:
                comput.save()
                mensaje = "Articulo de Computacion actualizado con exito"
            except:
                mensaje = "Ha ocurrido un error al actualizar el Articulo de Computacion"


            return render(request, "adminComputacion/actualizarComputacion.html", {"mensaje":mensaje})
        
        else:
            mensaje = "No se ha encontrado el Articulo ingresado"

            return render(request, "adminComputacion/actualizarComputacion.html", {"mensaje":mensaje})
    else:
        mensaje = "No se encontró el Articulo ingresado"

        return render(request, "adminComputacion/actualizarComputacion.html", {"mensaje":mensaje})

def eliminarComputacion(request):
    return render(request,"adminComputacion/eliminarComputacion.html")

def eliminaComputacion(request):
    
    mensaje = None
    try:
        compu = AppAdministracion_InsumosComputacionales.objects.get( numero_insumo = request.POST["numero_insumo"])
        compu.delete()
        mensaje = "Articulo eliminado"
        return render(request, "respuestaHtas.html",{"mensaje":mensaje})
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            mensaje = 'Articulo no existe'
            return render(request, "respuestaHtas.html",{"mensaje":mensaje})
        else:
            mensaje = 'Ha ocurrido un problema al tratar de eliminar el articulo'
        return render(request, "respuestaHtas.html",{"mensaje":mensaje})    






    

