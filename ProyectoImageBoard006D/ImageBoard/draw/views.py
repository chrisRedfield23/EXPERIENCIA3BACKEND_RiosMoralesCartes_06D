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
    return render(request, 'RegistroUsuario.html')
