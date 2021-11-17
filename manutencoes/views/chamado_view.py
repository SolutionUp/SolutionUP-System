from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from manutencoes.forms import FormChamado
from manutencoes.models import Chamado

class ChamadoListView(LoginRequiredMixin, ListView):
    model = Chamado
    paginate_by = 100
    template_name = 'chamado/chamado_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q') or ''
        object_list = self.model.objects.filter(
            Q(id__icontains=query) | 
            Q(responsavel__nome__icontains=query)
        )
        return object_list

class ChamadoDetailView(LoginRequiredMixin, DetailView):
    model = Chamado
    template_name = 'chamado/chamado_detail.html'

@login_required
def adicionar_chamado(request):
    if request.method == 'POST':
        form_chamado = FormChamado(request.POST)
        if form_chamado.is_valid():
            if form_chamado.data_fim_valid():
                form_chamado.save()
                messages.add_message(request, messages.SUCCESS, 'Chamado cadastrado!', extra_tags='success')
                return redirect('/chamados')
            else:
                messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
                return render(request, 'chamado/chamado_add.html', {'form_chamado': form_chamado})
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'chamado/chamado_add.html', {'form_chamado': form_chamado})
    else:
        form_chamado = FormChamado()
        return render(request, 'chamado/chamado_add.html', {'form_chamado': form_chamado})

@login_required
def remover_chamado(request, id):
    if request.method == 'GET':
        chamado = Chamado.objects.get(id=id)
        chamado.delete()
        return redirect('/chamados')
    else:
        return render(request, 'chamado/chamado_list.html')

@login_required
def alterar_chamado(request, id): 
    instance = get_object_or_404(Chamado, id=id)
    form_chamado = FormChamado(request.POST or None, instance=instance)    
    if request.method == 'POST':
        if form_chamado.is_valid():
                form_chamado.save()
                messages.add_message(request, messages.SUCCESS, 'Chamado alterado!', extra_tags='success')
                return redirect('/chamados')
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'chamado/chamado_add.html', {'form_chamado': form_chamado})
    else:
        return render(request, 'chamado/chamado_add.html', {'form_chamado': form_chamado})
