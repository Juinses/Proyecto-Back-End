from django.shortcuts import render, get_object_or_404, redirect
from .models import Juego, Genero
from .forms import JuegoForm

# Home: listar géneros
def home(request):
    generos = Genero.objects.all()
    return render(request, 'templatesrol/seleccion_rol.html', {'generos': generos})

# Listado de juegos por género + buscador
def juegos_por_genero(request, genero_id):
    genero = get_object_or_404(Genero, id=genero_id)
    juegos = genero.juegos.all()
    if query := request.GET.get("q"):
        juegos = juegos.filter(nombre__icontains=query)
    return render(request, 'templatesrol/tipos_rol.html', {'tipo': genero.nombre, 'juegos': juegos})

# Detalle del juego
def descripcion_rol(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    return render(request, 'templatesrol/descripcion_rol.html', {'juego': juego})

# Crear o editar juego
def manejar_juego(request, pk=None):
    juego = get_object_or_404(Juego, pk=pk) if pk else None
    if request.method == "POST":
        form = JuegoForm(request.POST, request.FILES, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JuegoForm(instance=juego)
    accion = 'Editar' if juego else 'Crear'
    return render(request, 'templatesrol/juegos/form.html', {'form': form, 'accion': accion})

# Eliminar juego
def eliminar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == "POST":
        juego.delete()
        return redirect('home')
    return render(request, 'templatesrol/juegos/eliminar.html', {'juego': juego})
