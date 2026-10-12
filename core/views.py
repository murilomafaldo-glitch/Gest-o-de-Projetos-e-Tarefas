from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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


def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)

        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('listar_projetos')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'core/formulario_projeto.html', {
        'form': form,
        'projeto': projeto
    })


def excluir_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        projeto.delete()
        messages.success(request, 'Projeto excluído com sucesso!')
        return redirect('listar_projetos')

    return render(request, 'core/confirmar_exclusao.html', {
        'projeto': projeto
    })
