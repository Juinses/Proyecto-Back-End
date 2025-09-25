from django.contrib import admin
from .models import companies

@admin.register(companies)
class companiesAdmin(admin.ModelAdmin):
    list_display = ("nombre",)  
    search_fields = ("nombre",)
