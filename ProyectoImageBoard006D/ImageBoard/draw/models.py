from django.db import models


# Create your models here.
class inicio_sesion(models.Model):
    correo = models.IntegerField(primary_key=True, verbose_name='correo')
    contraseña = models.CharField(max_length=20, verbose_name='contraseña')

    def _str_(self):
        return(self.correo)



class registro(models.Model):
    nombre  = models.CharField(max_length=20, verbose_name='nombre')
    apellido = models.CharField(max_length=20, verbose_name='apellido')
    correo_electronico = models.CharField(max_length=40,primary_key=True, verbose_name='correo_electronico')
    telefono  = models.IntegerField(max_length=10, verbose_name='telefono')
    fecha_nacimiento = models.CharField(max_length=10, verbose_name='fecha_nacimiento')
    direccion = models.CharField(max_length=50, verbose_name='direccion')
    region  = models.CharField(max_length=15, verbose_name='region')
    genero = models.CharField(max_length=9, verbose_name='genero')
    inicio_sesion = models.ForeignKey(inicio_sesion, on_delete=models.CASCADE)

    def _str_(self):
        return(self.nombre)
