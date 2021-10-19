from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from vendas.forms import FormComissaoPedido
from vendas.models import ComissaoPedido

class ComissaoPedidoListView(LoginRequiredMixin, ListView):
    model = ComissaoPedido
    paginate_by = 100
    template_name = 'comissao/comissao_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q') or ''
        object_list = self.model.objects.filter(
            Q(id__icontains=query) |
            Q(funcionario__nome__icontains=query)
        )
        return object_list

@login_required
def adicionar_comissao(request):
    if request.method == 'POST':
        form_comissao = FormComissaoPedido(request.POST)
        if form_comissao.is_valid():
            form_comissao.save()
            messages.add_message(request, messages.SUCCESS, 'Comissão cadastrada!', extra_tags='success')
            return redirect('/comissoes/adicionar')
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'comissao/comissao_add.html', {'form_comissao': form_comissao})
    else:
        form_comissao = FormComissaoPedido()
        return render(request, 'comissao/comissao_add.html', {'form_comissao': form_comissao})

@login_required
def remover_comissao(request, id):
    if request.method == 'GET':
        comissao = ComissaoPedido.objects.get(id=id)
        comissao.delete()
        return redirect('/comissoes')
    else:
        return render(request, 'comissao/comissao_list.html')

@login_required
def alterar_comissao(request, id):
    instance = get_object_or_404(ComissaoPedido, id=id)
    comissao = ComissaoPedido.objects.get(id=id)
    form_comissao = FormComissaoPedido(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form_comissao.is_valid():
            form_comissao.save()
            messages.add_message(request, messages.SUCCESS, 'Comissão alterada!', extra_tags='success')
            return redirect('/comissoes')
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'comissao/comissao_add.html', {'form_comissao': form_comissao})
    else:
        return render(request, 'comissao/comissao_add.html', {'form_comissao': form_comissao})