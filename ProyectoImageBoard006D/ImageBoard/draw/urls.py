from django.urls import path
from .views import MenuPrincipal02, Galeria02, QuienesSomos02, APIferiados, RegistroContacto, RegistroUsuario, home, InicioSesion

urlpatterns=[ 
    path('', MenuPrincipal02, name="MenuPrincipal02"),
    path('Galeria02', Galeria02, name="Galeria02"),
    path('QuienesSomos02', QuienesSomos02, name="QuienesSomos02"),
    path('APIferiados', APIferiados, name="APIferiados"),
    path('RegistroContacto',RegistroContacto, name="RegistroContacto"),
    path('RegistroUsuario', RegistroUsuario, name="RegistroUsuario"),
    path('home', home, name="home"),
    path('InicioSesion', InicioSesion, name="InicioSesion"),]