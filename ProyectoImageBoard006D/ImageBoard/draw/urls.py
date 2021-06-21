from django.urls import path
from .views import MenuPrincipal02, Galeria02, QuienesSomos02, APIferiados, RegistroContacto, RegistroUsuario, home, InicioSesion, ver, form_mod_registro, form_registro  

urlpatterns=[ 
    path('', MenuPrincipal02, name="MenuPrincipal02"),
    path('Galeria02', Galeria02, name="Galeria02"),
    path('QuienesSomos02', QuienesSomos02, name="QuienesSomos02"),
    path('APIferiados', APIferiados, name="APIferiados"),
    path('RegistroContacto',RegistroContacto, name="RegistroContacto"),
    path('RegistroUsuario', RegistroUsuario, name="RegistroUsuario"),
    path('home', home, name="home"),
    path('InicioSesion', InicioSesion, name="InicioSesion"),
    path('ver', ver, name="ver"),
    path('form_mod_registro', form_mod_registro, name="form_mod_registro"),
    path('form_registro', form_registro, name="form_registro"),]
