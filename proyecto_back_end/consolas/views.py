from django.shortcuts import render, get_object_or_404, redirect
from .models import companies, consola
from .forms import ConsolaForm

# Home: listado de empresas
def home_empresas(request):
    empresas = companies.objects.all()
    return render(
        request,
        'templates_consolas/seleccion_empresa.html',
        {'empresas': empresas}
    )

# Listado de consolas por empresa + buscador
def consolas_por_empresa(request, empresa_id):
    empresa = get_object_or_404(companies, id=empresa_id)
    consolas = empresa.consolas.all()

    if query := request.GET.get("q"):
        consolas = consolas.filter(nombre__icontains=query)

    return render(
        request,
        'templates_consolas/consolas.html',
        {'empresa': empresa, 'consolas': consolas}
    )

# Detalle de la consola
def descripcion_consola(request, consola_id):
    consola_obj = get_object_or_404(consola, id=consola_id)
    return render(request, 'templates_consolas/descripcion_consolas.html', {'consola': consola_obj})

# Crear o editar consola
def manejar_consola(request, pk=None):
    consola_obj = get_object_or_404(consola, pk=pk) if pk else None

    if request.method == "POST":
        form = ConsolaForm(request.POST, request.FILES, instance=consola_obj)
        if form.is_valid():
            consola_guardada = form.save()
            # Redirige al listado de consolas de la empresa correspondiente
            return redirect('consolas_por_empresa', empresa_id=consola_guardada.empresa.id)
    else:
        form = ConsolaForm(instance=consola_obj)

    accion = 'Editar' if consola_obj else 'Crear'
    return render(request, 'templates_consolas/consolas/form.html', {'form': form, 'accion': accion})

# Eliminar consola
def eliminar_consola(request, pk):
    consola_obj = get_object_or_404(consola, pk=pk)
    if request.method == "POST":
        empresa_id = consola_obj.empresa.id  # guardamos empresa antes de eliminar
        consola_obj.delete()
        return redirect('consolas_por_empresa', empresa_id=empresa_id)
    return render(request, 'templates_consolas/consolas/eliminar.html', {'consola': consola_obj})

# Lista de empresas
def lista_empresas(request):
    empresas = companies.objects.all()
    return render(request, 'templates_consolas/lista.html', {'empresas': empresas})
