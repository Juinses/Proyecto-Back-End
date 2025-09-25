from django.shortcuts import render, get_object_or_404, redirect
from .models import Juego, Genero
from .forms import JuegoForm


# Home: listar géneros
def home_juegos(request):
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
            juego_guardado = form.save()
            # Redirige a la lista del género correspondiente
            return redirect('juegos_por_genero', genero_id=juego_guardado.genero.id)
    else:
        form = JuegoForm(instance=juego)
    accion = 'Editar' if juego else 'Crear'
    return render(request, 'templatesrol/juegos/form.html', {'form': form, 'accion': accion})

# Eliminar juego
def eliminar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == "POST":
        genero_id = juego.genero.id  # Guardamos el género antes de eliminar
        juego.delete()
        return redirect('juegos_por_genero', genero_id=genero_id)
    return render(request, 'templatesrol/juegos/eliminar.html', {'juego': juego})

def home(request):
    return render(request, 'home.html')
