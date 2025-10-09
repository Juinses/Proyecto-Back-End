from django import forms
from .models import Company, Consola

# Formulario para Company
class EmpresaForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre de la empresa'
        })
    )
    pais_origen = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el país de origen'
        })
    )
    anio_salida = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el año de salida'
        })
    )
    cantidad_consolas = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Cantidad de consolas lanzadas'
        })
    )

    class Meta:
        model = Company
        fields = ['nombre', 'pais_origen', 'anio_salida', 'cantidad_consolas']


# Formulario para Consola
class ConsolaForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre de la consola'
        })
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Ingrese una breve descripción de la consola'
        })
    )
    imagen = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control'
        })
    )
    anio_salida = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Año de lanzamiento'
        })
    )
    ventas_totales = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ventas totales'
        })
    )
    juegos_vendidos = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Juegos vendidos'
        })
    )

    class Meta:
        model = Consola
        fields = ['nombre', 'descripcion', 'imagen', 'anio_salida', 'ventas_totales', 'juegos_vendidos']
