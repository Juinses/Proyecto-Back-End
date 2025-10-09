from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("nombre", "pais_origen", "anio_salida", "cantidad_consolas")
    search_fields = ("nombre",)