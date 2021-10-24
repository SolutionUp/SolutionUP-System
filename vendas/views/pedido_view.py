from django.contrib.messages.api import success
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from vendas.forms import FormPedido, FormPedidoItem
from vendas.models import Pedido, PedidoItem, Funcionario, ComissaoPedido
from django.http import Http404

class PedidoListView(LoginRequiredMixin, ListView):
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

class PedidoDetailView(LoginRequiredMixin, DetailView):
    model = Pedido
    template_name = 'pedido/pedido_detail.html'

@login_required
def adicionar_pedido(request):
    form_pedido = FormPedido(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form_pedido.is_valid():
            new_pedido = form_pedido.save()
            messages.add_message(request, messages.SUCCESS, 'Agora insira os itens do pedido!', extra_tags='success')
            return redirect(f'/pedidos/alterar/{new_pedido.id}')
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')       
    return render(request, 'pedido/pedido_add.html', {'form_pedido': form_pedido})

@login_required
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

@login_required
def alterar_pedido(request, id):
    instance = get_object_or_404(Pedido, id=id)
    pedido = Pedido.objects.get(id=id)
    itens = PedidoItem.objects.filter(pedido=id)
    total_itens = pedido.get_total_itens()
    form_pedido = FormPedido(request.POST or None, request.FILES or None, instance=instance)
    form_item = FormPedidoItem(request.POST or None)
    if request.method == 'POST':
        if form_pedido.is_valid():
            old_comprovante = Pedido.objects.get(id=pedido.id).comprovante.name
            if not old_comprovante:
                form_pedido.save()
            elif form_pedido.cleaned_data['comprovante'] != old_comprovante:
                pedido.comprovante.storage.delete(pedido.comprovante.name)
            funcionario = form_pedido.cleaned_data['funcionario']
            comissao = Funcionario.objects.get(id=funcionario.id).percentual_comissao
            valor_comissao = (comissao / 100) * total_itens
            if ComissaoPedido.objects.filter(pedido=pedido.id).exists():
                comissao_pedido = ComissaoPedido.objects.get(pedido=pedido.id)
                comissao_pedido.valor_comissao = valor_comissao
                comissao_pedido.save()
            else:
                comissao_pedido = ComissaoPedido.objects.create(pedido=pedido, funcionario=funcionario, valor_comissao=valor_comissao)
            
            form_pedido.save()
            messages.add_message(request, messages.SUCCESS, 'Pedido alterado!', extra_tags='success')
            return redirect(f'/pedidos/alterar/{pedido.id}')
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'pedido/pedido_edit.html', {'form': form_pedido})
    else:
        return render(request, 'pedido/pedido_edit.html', {'form_pedido': form_pedido, 'form_item' : form_item, 'pedido': pedido, 'itens': itens, 'total_itens': total_itens})

@login_required
def alterar_item(request, id_pedido):
    pedido = Pedido.objects.get(id=id_pedido)
    form_item = FormPedidoItem(request.POST or None)
    if request.method == 'POST':
        if form_item.is_valid():
            new_item = PedidoItem(
                pedido=pedido,
                produto=form_item.cleaned_data['produto'],
                quantidade=form_item.cleaned_data['quantidade']
            )
            if new_item.quantidade > new_item.produto.quantidade:
                messages.add_message(request, messages.ERROR, 'Quantidade de produtos informada maior que a disponível!', extra_tags='danger')
            else:
                new_item.produto.quantidade -= new_item.quantidade
                new_item.produto.save()
                
                item = PedidoItem.objects.filter(pedido=pedido, produto=new_item.produto)
                if item:
                    item[0].quantidade += new_item.quantidade
                    item[0].save() 
                else:
                    new_item.produto.save()
                    new_item.save()    
    return redirect(f'/pedidos/alterar/{id_pedido}')

@login_required
def remover_item(request, id_pedido, id_item):
    if request.method == 'GET':
        try:
            item = PedidoItem.objects.get(id=id_item)
            print(item)
            messages.add_message(request, messages.SUCCESS, 'Item removido!', extra_tags='success')
        except:
            messages.add_message(request, messages.ERROR, 'Não foi possível remover item do pedido!', extra_tags='danger')
            return redirect('/pedidos')                                    
        item.produto.quantidade += item.quantidade
        item.produto.save()
        item.delete()     
        return redirect(f'/pedidos/alterar/{id_pedido}')
