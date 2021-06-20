from django import forms
from django.forms import ModelForm, widgets
from .models import registro

class registroForm(ModelForm):

    class Meta:
        model = registro
        fields = ['nombre', 'apellido', 'correo_electronico', 'telefono', 'fecha_nacimiento',
        'direccion', 'region', 'genero', 'inicio_sesion']

        labels ={
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo_electronico': 'Correo',
            'telefono' : 'Telefono',
            'fecha_nacimiento': 'Fecha Nacimiento',
            'direccion': 'Dirección',
            'region': 'Región',
            'genero': 'Género',
            'inicio_sesion': 'Inicio Sesión',

        }

        widgets ={

            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Digite nombre',
                    'id': 'nombre'
                }
            ),

            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Digite apellido',
                    'id': 'apellido'
                }
            ),

            'correo_electronico': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Digite correo',
                    'id': 'correo_electronico'
                }
            ),

            'telefono': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Digite teléfono',
                    'id': 'telefono'
                }
            ),

            'fecha_nacimiento': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Digite fecha nacimiento',
                    'id': 'fecha_nacimiento'
                }
            ),

            'direccion': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Digite dirección',
                    'id': 'direccion'
                }
            ),

            'region': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Digite región',
                    'id': 'region'
                }
            ),

            'genero': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Digite género',
                    'id': 'genero'
                }
            ),

            'inicio_sesion': forms.Select(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Digite Inicio Sesión',
                    'id': 'inicio_sesion'
                }
            ),

        }