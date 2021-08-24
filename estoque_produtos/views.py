from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q
from .forms import FormProduto
from .models import Produto

class ProdutoListView(ListView):
    model = Produto
    paginate_by = 100

    def get_queryset(self):
        query = self.request.GET.get('q') or ''
        object_list = Produto.objects.filter(
            Q(codigo__icontains=query) |
            Q(nome__icontains=query) |
            Q(marca__icontains=query)
        )
        return object_list

class ProdutoDetailView(DetailView):
    model = Produto

def adicionar_produto(request):
    if request.method == 'POST':
        form = FormProduto(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Produto cadastrado!', extra_tags='success')
            return redirect('/produtos/adicionar')
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'estoque_produtos/produto_add.html', {'form': form})
    else:
        form = FormProduto()
        return render(request, 'estoque_produtos/produto_add.html', {'form': form})

def remover_produto(request, codigo):
    if request.method == 'GET':
        produto = Produto.objects.get(codigo=codigo)
        produto.delete()
        return redirect('/produtos')
    else:
        return render(request, 'estoque_produtos/produto_list.html')

def alterar_produto(request, codigo): 
    instance = get_object_or_404(Produto, codigo=codigo)
    form = FormProduto(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Produto alterado!', extra_tags='success')
            return redirect('/produtos')
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'estoque_produtos/produto_add.html', {'form': form})
    else:
        return render(request, 'estoque_produtos/produto_add.html', {'form': form})
