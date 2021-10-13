from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from vendas.forms import FormPedido
from vendas.models import Pedido
from django.http import Http404

class PedidoListView(LoginRequiredMixin, ListView):
    model = Pedido
    paginate_by = 100
    template_name = 'pedido/pedido_list.html'

    def get_queryset(self):
        if self.request.user.has_perm('vendas.view_pedido'):
            query = self.request.GET.get('q') or ''
            object_list = self.model.objects.filter(
                Q(id__icontains=query) |
                Q(status__icontains=query)
            )
            return object_list
        raise Http404
        

class PedidoDetailView(LoginRequiredMixin, DetailView):
    model = Pedido
    template_name = 'pedido/pedido_detail.html'

@login_required
def adicionar_pedido(request):
    if request.user.has_perm('vendas.add_pedido'):
        if request.method == 'POST':
            form_pedido = FormPedido(request.POST, request.FILES)
            if form_pedido.is_valid():
                form_pedido.save()
                messages.add_message(request, messages.SUCCESS, 'Pedido cadastrado!', extra_tags='success')
                return redirect('/pedidos/adicionar')
            else:
                messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
                return render(request, 'pedido/pedido_add.html', {'form': form_pedido})
        else:
            form_pedido = FormPedido()
            return render(request, 'pedido/pedido_add.html', {'form': form_pedido})
    raise Http404

@login_required
def remover_pedido(request, id):
    if request.user.has_perm('vendas.delete_pedido'):
        if request.method == 'GET':
            pedido = Pedido.objects.get(id=id)
            comprovante = Pedido.objects.get(id=pedido.id).comprovante.name
            if comprovante:
                pedido.comprovante.storage.delete(pedido.comprovante.name)
            pedido.delete()
            return redirect('/pedidos')
        else:
            return render(request, 'pedido/pedido_list.html')
    raise Http404

@login_required
def alterar_pedido(request, id):
    if request.user.has_perm('vendas.change_pedido'):
        instance = get_object_or_404(Pedido, id=id)
        pedido = Pedido.objects.get(id=id)
        form_pedido = FormPedido(request.POST or None, request.FILES or None, instance=instance)
        if request.method == 'POST':
            if form_pedido.is_valid():
                old_comprovante = Pedido.objects.get(id=pedido.id).comprovante.name
                if not old_comprovante:
                    form_pedido.save()
                elif form_pedido.cleaned_data['comprovante'] != old_comprovante:
                    pedido.comprovante.storage.delete(pedido.comprovante.name)
                form_pedido.save()
                messages.add_message(request, messages.SUCCESS, 'Pedido alterado!', extra_tags='success')
                return redirect('/pedidos')
            else:
                messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
                return render(request, 'pedido/pedido_add.html', {'form': form_pedido})
        else:
            return render(request, 'pedido/pedido_add.html', {'form': form_pedido})
    raise Http404
