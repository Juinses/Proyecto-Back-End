from django.shortcuts import render, get_object_or_404, redirect
from .models import Juego, Plataforma
from .forms import JuegoForm

# Home: listar plataformas
def home_juegos(request):
    plataformas = Plataforma.objects.all()
    return render(request, 'templatesrol/seleccion_rol.html', {'plataformas': plataformas})

# Listado de juegos por plataforma + buscador
def juegos_por_plataforma(request, plataforma_id):
    plataforma = Plataforma.objects.get(id=plataforma_id)
    juegos = Juego.objects.filter(plataforma=plataforma)
    return render(request, 'templatesrol/tipos_rol.html', {  
        'plataforma': plataforma,
        'juegos': juegos
    })

# Detalle del juego
def descripcion_rol(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    return render(request, 'templatesrol/descripcion_rol.html', {'juego': juego})

# Crear o editar juego
def manejar_juego(request, pk=None, plataforma_id=None):
    # Si pk viene, estamos editando; si no, estamos creando
    juego = get_object_or_404(Juego, pk=pk) if pk else None

    # Si hay plataforma_id, lo usamos para asignar el juego
    plataforma = get_object_or_404(Plataforma, id=plataforma_id) if plataforma_id else None

    if request.method == "POST":
        form = JuegoForm(request.POST, request.FILES, instance=juego)
        if form.is_valid():
            juego_guardado = form.save(commit=False)
            if plataforma:  # Solo asignamos plataforma si viene
                juego_guardado.plataforma = plataforma
            juego_guardado.save()
            
            # Redirige a la lista de juegos de la plataforma si hay plataforma_id
            if plataforma:
                return redirect('juegos_por_plataforma', plataforma_id=plataforma.id)
            else:
                return redirect('home_juegos')  # O donde quieras redirigir si no hay plataforma
    else:
        form = JuegoForm(instance=juego)

    accion = 'Editar' if juego else 'Crear'

    return render(request, 'templatesrol/juegos/form.html', {
        'form': form,
        'accion': accion,
        'plataforma': plataforma
    })

# Eliminar juego
def eliminar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == "POST":
        plataforma_id = juego.plataforma.id  # Guardamos la plataforma antes de eliminar
        juego.delete()
        return redirect('juegos_por_plataforma', plataforma_id=plataforma_id)
    return render(request, 'templatesrol/juegos/eliminar.html', {'juego': juego})


# Página principal
def home(request):
    return render(request, 'home.html')
