from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm

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

def listar_tarefas(request):
    tarefas = Tarefa.objects.select_related('projeto').all()
    return render(request, 'core/listar_tarefas.html', {
        'tarefas': tarefas
    })

def cadastrar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa cadastrada com sucesso!')
            return redirect('listar_tarefas')
    else:
        form = TarefaForm()

    return render(request, 'core/formulario_tarefa.html', {
        'form': form,
        'titulo': 'Cadastrar tarefa'
    })

def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('listar_tarefas')
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, 'core/formulario_tarefa.html', {
        'form': form,
        'titulo': 'Editar tarefa'
    })

def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('listar_tarefas')

    return render(request, 'core/confirmar_exclusao_tarefa.html', {
        'tarefa': tarefa
    })
