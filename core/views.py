from django.shortcuts import render, redirect
from .models import Mascotas,Estado,Raza
#importamos la mensajeria de django
from django.contrib import messages
#nuevo comentario
from django.contrib.auth.decorators import login_required
#un decorador nos permite agregar funcionalidad a un metodo
from fcm_django.models import FCMDevice

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def listado(request):
    #consultaremos a la base de datos para decirle que me entregue
    #todos los automoviles
    mascotas = Mascotas.objects.all()
    #llamamos al template y junton con ello le pasamos
    #datos, en este caso el listado de autos que existe en la BBDD
    return render(request, 'core/listado_mascotas.html',{
        'mascotas':mascotas
    })

@login_required
def formulario(request):
    razas = Raza.objects.all()
    #declaramos el diccionario de variables que se enviaran al template
    variables = {
        'razas':razas
    }

    #preguntaremos si la peticion es POST
    if request.POST:
        #instanciar un Automovil
        mascotas = Mascotas()
        mascotas.nombre_mascota = request.POST.get('txtPatente')
        mascotas.raza = request.POST.get('txtModelo')
        mascotas.Estado = request.POST.get('txtAnio')
        #instanciamos una Marca
        raza = Raza()
        raza.raza = request.POST.get('cBoMarca')
        #dejamos el objeto marca dentro del auto
        mascotas.raza = raza
        #teniendo todos los datos capturados desde
        #el template, guardamos el automovil en la BBDD
        try:
            mascotas.save()

            #obtenemos todos los dispositivos
            dispositivos = FCMDevice.objects.all()
            #a cada dispositivo se le envia una notificacion
            dispositivos.send_message(
                title="Alerta MisPerris",
                body="Una nueva mascota ha sido agregado",
                icon="/static/core/img/logo.png"
            )
            
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"

    return render(request, 'core/formulario_mascotas.html',variables)


def eliminar(request, id):

    #para eliminar es necesario primero buscar el automovil
    mascotas = Mascotas.objects.get(id=id)

    #una vez encontrado el automovil se procede a eliminarlo
    try:
        mascotas.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje ="No se ha podido eliminar"
        messages.error(request, mensaje)
        
    #el redirect lo redirige por alias de una ruta
    return redirect(to="listado")

def modificar_automovil(request, id):

    raza = Raza.objects.all()
    #buscamos el automovil en la BBDD por su ID
    mascotas = Mascotas.objects.get(id=id)
    variables = {
        'raza':raza,
        'mascotas':mascotas
    }

    if request.POST:
        #si la peticion es POST recibimos las variables
        mascotas = Mascotas()
        mascotas.nombre_mascota =  request.POST.get('txtId')
        mascotas.raza = request.POST.get('txtPatente')
        mascotas.genero= request.POST.get('txtModelo')
        mascotas.fecha_ingreso = int(request.POST.get('txtAnio'))
        mascotas.fecha_nacimiento = int(request.POST.get('txtAnio'))
        #para recibir la marca creamos un objeto de tipo Marca
        raza = Raza()
        raza.raza = request.POST.get('cboMarca')
        #le pasamos la marca completa al automovil
        mascotas.raza = raza

        #ahora procederemos a actualizar el automovil
        try:
            mascotas.save()
            messages.success(request, "Actualizado correctamente")
        except:
            messages.error(request, "No se ha podido actualizar")

        #le haremos un redirect al usuario de vuelta hacia el listado   
        return redirect('listado')

    return render(request, 'core/modificar_mascotas.html', variables)
