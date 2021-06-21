from django.shortcuts import render


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

    return render(request, 'draw/ver.html', context={'registro':registro})

def form_registro(request):
    if request.method=="POST":
        registro_form = registroForm(request.POST)
        if registro_form.is_valid():
            registro_form.save() #Reemplaza el insert en django
            return redirect('home')
        else:
            registro_form=registroForm()
        return render(request, 'draw/form_registro.html',
        {'registro_form':registro_form})

def form_mod_registro(request,id):
    regisstro = registro.objects.get(nombre=nombre)

    datos ={
        'form': registroForm(instance=registro)
    }
    if request.method == 'POST': 
        formulario = registroForm(data=request.POST, instance = registro)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'draw/form_mod_registro.html', datos)