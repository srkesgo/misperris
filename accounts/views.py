from django.shortcuts import render
from .forms import CustomUserCreationForm

# Create your views here.

def register(request):

    variables = {
        'form':CustomUserCreationForm
    }

    if request.POST:
        #le pasamos al formulario de registro
        #todo lo que el usuario ingreso en el navegador
        form  = CustomUserCreationForm(request.POST)
        #preguntaremos si el formulario es valido
        if form.is_valid():
            #si es valido le diremos que guarde los
            #datos en la BBDD
            form.save()
            variables['mensaje'] = "Usuario registrado!"
        else:
            variables['mensaje'] = "No se ha podido registrar"
            #si hay errores de validacion debemos volver a enviar
            #el formulario al template ya que este lleva consigo
            #los mensajes de validacion
            variables['form'] = form

    return render(request, 'accounts/register.html', variables)