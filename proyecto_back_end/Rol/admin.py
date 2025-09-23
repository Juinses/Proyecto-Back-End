from django.contrib import admin
from django.utils.html import format_html
from .models import Genero, Juego

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)

