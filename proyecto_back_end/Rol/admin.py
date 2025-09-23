from django.contrib import admin
from django.utils.html import format_html
from .models import Genero, Juego

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "genero", "mostrar_imagen")
    list_filter = ("genero",)
    search_fields = ("nombre", "descripcion")

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="50" height="50" />', obj.imagen.url)
        return "Sin imagen"
    mostrar_imagen.short_description = "Imagen"
