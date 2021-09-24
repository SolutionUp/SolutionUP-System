from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q
from vendas.forms import FormPedido
from vendas.models import Pedido

class PedidoListView(ListView):
    model = Pedido
    paginate_by = 100
    template_name = 'pedido/pedido_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q') or ''
        object_list = self.model.objects.filter(
            Q(id__icontains=query) |
            Q(status__icontains=query)
        )
        return object_list

class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedido/pedido_detail.html'

def adicionar_pedido(request):
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

def remover_pedido(request, id):
    if request.method == 'GET':
        pedido = Pedido.objects.get(id=id)
        comprovante = Pedido.objects.get(id=pedido.id).comprovante.name
        if comprovante:
            pedido.comprovante.storage.delete(pedido.comprovante.name)
        pedido.delete()
        return redirect('/pedidos')
    else:
        return render(request, 'pedido/pedido_list.html')

def alterar_pedido(request, id):
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