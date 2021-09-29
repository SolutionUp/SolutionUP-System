from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from manutencoes.forms import FormTerceiro
from manutencoes.models import Terceiro

class TerceiroListView(ListView):
    model = Terceiro
    paginate_by = 100
    template_name = 'terceiro/terceiro_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q') or ''
        object_list = self.model.objects.filter(
            Q(nome__icontains=query) | 
            Q(ramo__icontains=query)
        )
        return object_list

class TerceiroDetailView(DetailView):
    model = Terceiro

@login_required
def adicionar_terceiro(request):
    if request.method == 'POST':
        form_terceiro = FormTerceiro(request.POST)
        if form_terceiro.is_valid():
            form_terceiro.save()
            messages.add_message(request, messages.SUCCESS, 'Terceiro cadastrado!', extra_tags='success')
            return redirect('/terceiros/adicionar')
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'terceiro/terceiro_add.html', {'form': form_terceiro})
    else:
        form_terceiro = FormTerceiro()
        return render(request, 'terceiro/terceiro_add.html', {'form': form_terceiro})

@login_required
def remover_terceiro(request, id):
    if request.method == 'GET':
        terceiro = Terceiro.objects.get(id=id)
        terceiro.delete()
        return redirect('/terceiros')
    else:
        return render(request, 'terceiro/terceiro_list.html')

@login_required
def alterar_terceiro(request, id): 
    instance = get_object_or_404(Terceiro, id=id)
    form_terceiro = FormTerceiro(request.POST or None, instance=instance)
    
    if request.method == 'POST':
        if form_terceiro.is_valid():
            form_terceiro.save()
            messages.add_message(request, messages.SUCCESS, 'Terceiro alterado!', extra_tags='success')
            return redirect('/terceiros')
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'terceiro/terceiro_add.html', {'form': form_terceiro})
    else:
        return render(request, 'terceiro/terceiro_add.html', {'form': form_terceiro})