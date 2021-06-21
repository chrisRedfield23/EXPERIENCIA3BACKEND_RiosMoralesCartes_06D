from django.shortcuts import render, redirect, get_object_or_404
from .forms import registroForm
from .models import inicio_sesion, registro


# Create your views here.

def MenuPrincipal02(request):
    return render(request, 'MenuPrincipal02.html')

def Galeria02(request):
    return render(request, 'Galeria02.html')

def QuienesSomos02(request):
    return render(request, 'QuienesSomos02.html')

def APIferiados(request):
    return render(request, 'APIferiados.html') 

def RegistroContacto(request):
    return render(request, 'RegistroContacto.html')

def RegistroUsuario(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'RegistroUsuario.html')

def InicioSesion(request):
    return render(request, 'InicioSesion.html')

def ver(request):
    regisstro = registro.objects.all()
    return render(request, 'draw/ver.html', context={'registro':regisstro})

def form_mod_registro(request, correo):
    Registro_forms=registro.get (correo=correo)
    datos ={'form': registroForm(instance=registro_forms)}
    if request.method == 'POST': 
        formulario = registroForm(Data=request.post , instance =registro_forms)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'draw/form_mod_registro.html', datos)


def form_registro(request):
    if request.method=="POST":
            registro_form = registroForm(request.POST)
            if registro_form.is_valid():
                registro_form.save() #Reemplaza el insert en django
                return render('home')
    else:
        registro_form=registroForm()
    return render(request, 'draw/form_registro.html',
    {'registro_form':registro_form})

 
def form_del_registro(request,correo):
    registros = get_object_or_404(registros, correo=correo)
    registros.delete()
    return redirect('ver')





