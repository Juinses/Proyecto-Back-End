from django.shortcuts import render
from Rol import models as DatosRol 

def seleccion_rol(request):
    data = {
        "juegos_rol": DatosRol.juegos_rol
    }
    return render(request, 'templatesrol/seleccion_rol.html',data)

def Tipos_rol(request):
    return render(request, 'Tipos_rol.html')

def descripcion_rol(request):
    return render(request, 'descripcion_rol.html')
