from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Juego, Plataforma
from .forms import JuegoForm

# ---------------------- Helpers ----------------------
def es_admin(user):
    return user.is_staff

# ---------------------- Vistas públicas ----------------------
def home_juegos(request):
    plataformas = Plataforma.objects.all()
    return render(request, 'templatesrol/seleccion_rol.html', {'plataformas': plataformas})

def juegos_por_plataforma(request, plataforma_id):
    plataforma = get_object_or_404(Plataforma, id=plataforma_id)
    juegos = Juego.objects.filter(plataforma=plataforma)

    # Guardar la URL anterior
    previous_url = request.META.get('HTTP_REFERER', '/')

    return render(request, 'templatesrol/tipos_rol.html', {
        'plataforma': plataforma,
        'juegos': juegos,
        'previous_url': previous_url
    })

def descripcion_rol(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    return render(request, 'templatesrol/descripcion_rol.html', {'juego': juego})

def home(request):
    return render(request, 'home.html')

# ---------------------- Logout ----------------------
def logout_view(request):
    logout(request)
    return redirect('home')

# ---------------------- CRUD juegos (solo admin) ----------------------
@login_required
@user_passes_test(es_admin, login_url='home')  # Redirige a home si no es admin
def manejar_juego(request, pk=None, plataforma_id=None):
    juego = get_object_or_404(Juego, pk=pk) if pk else None
    plataforma = get_object_or_404(Plataforma, id=plataforma_id) if plataforma_id else None

    if request.method == "POST":
        form = JuegoForm(request.POST, request.FILES, instance=juego)
        if form.is_valid():
            juego_guardado = form.save(commit=False)
            if plataforma:
                juego_guardado.plataforma = plataforma
            juego_guardado.save()
            
            # Redirige a la lista de juegos de la plataforma si aplica
            return redirect('juegos_por_plataforma', plataforma_id=plataforma.id) if plataforma else redirect('home_juegos')
    else:
        form = JuegoForm(instance=juego)

    accion = 'Editar' if juego else 'Crear'

    return render(request, 'templatesrol/juegos/form.html', {
        'form': form,
        'accion': accion,
        'plataforma': plataforma
    })

@login_required
@user_passes_test(es_admin, login_url='home')
def eliminar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == "POST":
        plataforma_id = juego.plataforma.id
        juego.delete()
        return redirect('juegos_por_plataforma', plataforma_id=plataforma_id)
    return render(request, 'templatesrol/juegos/eliminar.html', {'juego': juego})
