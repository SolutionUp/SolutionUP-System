from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from vendas.forms import FormFuncionario, FormCargo
from vendas.models import Funcionario, Cargo

class FuncionarioListView(LoginRequiredMixin, ListView):
    model = Funcionario
    paginate_by = 100
    template_name = 'funcionario/funcionario_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q') or ''
        object_list = self.model.objects.filter(
            Q(nome__icontains=query) |
            Q(cpf__icontains=query)
        )
        return object_list

@login_required
def adicionar_funcionario(request):
    form_cargo = FormCargo()
    if request.method == 'POST':
        form_funcionario = FormFuncionario(request.POST)
        if form_funcionario.is_valid():
            if len(form_funcionario.cleaned_data['cpf']) == 11:
                form_funcionario.save()
                messages.add_message(request, messages.SUCCESS, 'Funcionário cadastrado!', extra_tags='success')
                return redirect('/funcionarios/adicionar')
            else:
                messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
                return render(request, 'funcionario/funcionario_add.html', {'form_funcionario': form_funcionario, 'form_cargo': form_cargo})
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'funcionario/funcionario_add.html', {'form_funcionario': form_funcionario, 'form_cargo': form_cargo})
    else:
        form_funcionario = FormFuncionario()
        return render(request, 'funcionario/funcionario_add.html', {'form_funcionario': form_funcionario, 'form_cargo': form_cargo})

@login_required
def remover_funcionario(request, id):
    if request.method == 'GET':
        funcionario = Funcionario.objects.get(id=id)
        funcionario.delete()
        return redirect('/funcionarios')
    else:
        return render(request, 'funcionario/funcionario_list.html')

@login_required
def alterar_funcionario(request, id): 
    instance = get_object_or_404(Funcionario, id=id)
    funcionario = Funcionario.objects.get(id=id)
    form_funcionario = FormFuncionario(request.POST or None, instance=instance)
    form_cargo = FormCargo()
    if request.method == 'POST':
        if form_funcionario.is_valid():
            form_funcionario.save()
            messages.add_message(request, messages.SUCCESS, 'Funcionário alterado!', extra_tags='success')
            return redirect('/funcionarios')
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'funcionario/funcionario_add.html', {'form_funcionario': form_funcionario, 'form_cargo': form_cargo})
    else:
        return render(request, 'funcionario/funcionario_add.html', {'form_funcionario': form_funcionario, 'form_cargo': form_cargo})

@login_required
def adicionar_cargo(request):
    if request.method == 'POST':
        form_cargo = FormCargo(request.POST)
        if form_cargo.is_valid():
            form_cargo.save()
            messages.add_message(request, messages.SUCCESS, 'Cargo cadastrado!', extra_tags='success')
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
    return redirect('/funcionarios/adicionar')