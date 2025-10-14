from django import forms
from .models import Juego, Plataforma
from django.utils import timezone


class JuegoForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre del juego'
        })
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Ingrese una breve descripción del juego'
        })
    )
    imagen = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = Juego
        fields = ['nombre', 'descripcion', 'imagen']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if not nombre:
            raise forms.ValidationError("El nombre del juego no puede estar vacío.")
        if len(nombre) > 50:
            raise forms.ValidationError("El nombre no puede tener más de 50 caracteres.")
        if Juego.objects.filter(nombre__iexact=nombre).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise forms.ValidationError("Ya existe un juego con este nombre.")
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion', '').strip()
        if descripcion and len(descripcion) < 20:
            raise forms.ValidationError("La descripción debe tener al menos 20 caracteres.")
        if len(descripcion) > 500:
            raise forms.ValidationError("La descripción no puede tener más de 500 caracteres.")
        return descripcion

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if imagen:
            ext = imagen.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png']:
                raise forms.ValidationError("Solo se permiten imágenes JPG o PNG.")
            if imagen.size > 2 * 1024 * 1024:
                raise forms.ValidationError("La imagen no puede superar 2MB.")
        return imagen