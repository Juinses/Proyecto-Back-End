from django.contrib import admin
from .models import Plataforma

@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)

