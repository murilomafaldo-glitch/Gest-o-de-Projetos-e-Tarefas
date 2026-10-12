from django.shortcuts import render, redirect
from .models import Projeto
from .forms import ProjetoForm

def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/listar_projetos.html', {
        'projetos': projetos
    })

def cadastrar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_projetos')
    else:
        form = ProjetoForm()

    return render(request, 'core/formulario_projeto.html', {
        'form': form
    })
