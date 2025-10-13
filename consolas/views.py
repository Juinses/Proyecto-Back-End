from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Company, Consola
from .forms import ConsolaForm

# ---------------------- Helpers ----------------------
def es_admin(user):
    return user.is_staff

# ---------------------- Vistas públicas ----------------------
def home_companies(request):
    companies = Company.objects.all()
    return render(request, 'templates_consolas/seleccion_empresa.html', {'companies': companies})

def consolas_por_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    consolas = company.consolas.all()  # usa related_name="consolas"

    if query := request.GET.get("q"):
        consolas = consolas.filter(nombre__icontains=query)

    return render(request, 'templates_consolas/consolas.html', {
        'company': company,
        'consolas': consolas
    })

def descripcion_consola(request, consola_id):
    consola = get_object_or_404(Consola, id=consola_id)
    company = consola.empresa
    return render(request, 'templates_consolas/descripcion_consolas.html', {
        'consola': consola,
        'company': company
    })

def lista_companies(request):
    companies = Company.objects.all()
    return render(request, 'templates_consolas/lista.html', {'companies': companies})

# ---------------------- CRUD consolas (solo admin) ----------------------
@login_required
@user_passes_test(es_admin, login_url='home_companies')
def manejar_consola(request, pk=None, company_id=None):
    consola = get_object_or_404(Consola, pk=pk) if pk else None
    company = get_object_or_404(Company, id=company_id) if company_id else None

    if request.method == "POST":
        form = ConsolaForm(request.POST, request.FILES, instance=consola)
        if form.is_valid():
            consola_guardada = form.save(commit=False)
            if company:
                consola_guardada.empresa = company
            consola_guardada.save()
            return redirect('consolas_por_company', company_id=company.id) if company else redirect('home_companies')
    else:
        form = ConsolaForm(instance=consola)

    accion = 'Editar' if consola else 'Crear'

    return render(request, 'templates_consolas/consolas/form.html', {
        'form': form,
        'accion': accion,
        'company': company
    })

@login_required
@user_passes_test(es_admin, login_url='home_companies')
def eliminar_consola(request, pk):
    consola_obj = get_object_or_404(Consola, pk=pk)
    empresa_id = consola_obj.empresa.id if consola_obj.empresa else None

    if request.method == "POST":
        consola_obj.delete()
        if empresa_id:
            return redirect('consolas_por_company', company_id=empresa_id)
        return redirect('home_companies')

    return render(request, 'templates_consolas/consolas/eliminar.html', {'consola': consola_obj})
