
# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from .forms import ProyectoForm
from django.contrib.auth.decorators import login_required
from .models import Proyecto
@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyectos:lista_proyectos')  # Asegúrate de tener esta URL
    else:
        form = ProyectoForm()

    return render(request, 'proyectos/crear.html', {'form': form})

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos/lista.html', {'proyectos': proyectos})

def editar_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('proyectos:lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)

    return render(request, 'proyectos/editar.html', {'form': form})

def eliminar_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    proyecto.delete()
    return redirect('proyectos:lista_proyectos')