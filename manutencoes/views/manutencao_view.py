from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from manutencoes.forms import FormManutencao
from manutencoes.models import Manutencao

class ManutencaoListView(LoginRequiredMixin, ListView):
    model = Manutencao
    paginate_by = 100
    template_name = 'manutencao/manutencao_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q') or ''
        object_list = self.model.objects.filter(
            Q(id__icontains=query) | 
            Q(responsavel__nome__icontains=query)
        )
        return object_list

class ManutencaoDetailView(LoginRequiredMixin, DetailView):
    model = Manutencao
    template_name = 'manutencao/manutencao_detail.html'

@login_required
def adicionar_manutencao(request):
    if request.method == 'POST':
        form_manutencao = FormManutencao(request.POST)
        if form_manutencao.is_valid():
            if form_manutencao.data_conclusao_valid():
                form_manutencao.save()
                messages.add_message(request, messages.SUCCESS, 'Manutenção cadastrada!', extra_tags='success')
                return redirect('/manutencoes')
            else:
                messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
                return render(request, 'manutencao/manutencao_add.html', {'form_manutencao': form_manutencao})
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'manutencao/manutencao_add.html', {'form_manutencao': form_manutencao})
    else:
        form_manutencao = FormManutencao()
        return render(request, 'manutencao/manutencao_add.html', {'form_manutencao': form_manutencao})

@login_required
def remover_manutencao(request, id):
    if request.method == 'GET':
        manutencao = Manutencao.objects.get(id=id)
        manutencao.delete()
        return redirect('/manutencoes')
    else:
        return render(request, 'manutencao/manutencao_list.html')

@login_required
def alterar_manutencao(request, id): 
    instance = get_object_or_404(Manutencao, id=id)
    form_manutencao = FormManutencao(request.POST or None, instance=instance)    
    if request.method == 'POST':
        if form_manutencao.is_valid():
            if form_manutencao.data_conclusao_valid():
                form_manutencao.save()
                messages.add_message(request, messages.SUCCESS, 'Manutenção alterada!', extra_tags='success')
                return redirect('/manutencoes')
            else:
                messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
                return render(request, 'manutencao/manutencao_add.html', {'form_manutencao': form_manutencao})
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'manutencao/manutencao_add.html', {'form_manutencao': form_manutencao})
    else:
        return render(request, 'manutencao/manutencao_add.html', {'form_manutencao': form_manutencao})
