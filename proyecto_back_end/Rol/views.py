from django.shortcuts import render
from Rol import models as DatosRol

def seleccion_rol(request):
    # Pasamos todo el diccionario de tipos de rol al template
    data = {
        "juegos_rol": DatosRol.juegos_rol,
    }
    return render(request, 'templatesrol/seleccion_rol.html', data)

def Tipos_rol(request, tipo):
    # Obtenemos la lista de juegos para el tipo seleccionado
    juegos = DatosRol.juegos_rol.get(tipo, [])
    context = {
        "tipo": tipo,
        "juegos": juegos,
    }
    return render(request, 'templatesrol/Tipos_rol.html', context)

def descripcion_rol(request, tipo, juego_nombre):
    # Obtener la lista de juegos del tipo
    juegos = DatosRol.juegos_rol.get(tipo, [])

    # Buscar el juego por nombre
    juego = next((j for j in juegos if j["nombre"] == juego_nombre), None)

    # Pasar al template
    context = {
        "juego": juego
    }

    return render(request, 'templatesrol/descripcion_rol.html', context)