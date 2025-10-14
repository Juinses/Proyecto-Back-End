from django import forms
from .models import Company, Consola
from django.utils import timezone

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
        required=True,  # Cambié a obligatorio
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ventas totales'
        })
    )
    juegos_vendidos = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Juegos vendidos'
        })
    )

    labels = {
        'nombre': 'Nombre:',
        'descripcion': 'Descripción:',
        'imagen': 'Imagen:',
        'anio_salida': 'Año de lanzamiento:',
        'ventas_totales': 'Ventas totales:',
        'juegos_vendidos': 'Juegos vendidos:'
    }

    class Meta:
        model = Consola
        fields = ['nombre', 'descripcion', 'imagen', 'anio_salida', 'ventas_totales', 'juegos_vendidos']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if not nombre:
            raise forms.ValidationError("El nombre no puede estar vacío.")
        if len(nombre) > 50:
            raise forms.ValidationError("El nombre no puede tener más de 50 caracteres.")
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion', '').strip()
        if not descripcion:
            raise forms.ValidationError("La descripción no puede estar vacía.")
        if len(descripcion) > 500:
            raise forms.ValidationError("La descripción no puede tener más de 500 caracteres.")
        return descripcion

    def clean_ventas_totales(self):
        ventas = self.cleaned_data.get('ventas_totales')
        if ventas is None:
            raise forms.ValidationError('El campo ventas totales no puede estar vacío.')
        if ventas < 0:
            raise forms.ValidationError('Las ventas totales no pueden ser negativas.')
        return ventas

    def clean_juegos_vendidos(self):
        juegos = self.cleaned_data.get('juegos_vendidos')
        ventas = self.cleaned_data.get('ventas_totales')
        if juegos is not None and juegos < 0:
            raise forms.ValidationError('Los juegos vendidos no pueden ser negativos.')
        if juegos is not None and ventas is not None and juegos > ventas:
            raise forms.ValidationError('Los juegos vendidos no pueden ser mayores que las ventas totales.')
        return juegos

    def clean_anio_salida(self):
        anio = self.cleaned_data.get('anio_salida')
        current_year = timezone.now().year
        if anio > current_year:
            raise forms.ValidationError(f'El año de salida no puede ser mayor que el año actual ({current_year}).')
        if anio < 1950:
            raise forms.ValidationError('El año de salida debe ser mayor o igual a 1950.')
        return anio
