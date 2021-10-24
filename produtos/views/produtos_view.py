import io
import csv
from datetime import datetime
from reportlab.pdfgen import canvas
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from produtos.forms import FormProduto, FormCategoriaProduto
from produtos.models import Produto, CategoriaProduto
from django.http import Http404

class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    paginate_by = 100

    def get_queryset(self):
        query = self.request.GET.get('q') or ''
        object_list = self.model.objects.filter(
            Q(codigo__icontains=query) |
            Q(nome__icontains=query) |
            Q(marca__icontains=query)
        )
        return object_list

class ProdutoDetailView(DetailView):
    model = Produto

@login_required
def adicionar_produto(request):
    form_categoria = FormCategoriaProduto()
    if request.method == 'POST':
        form_produto = FormProduto(request.POST, request.FILES)
        if form_produto.is_valid():
            form_produto.save()
            messages.add_message(request, messages.SUCCESS, 'Produto cadastrado!', extra_tags='success')
            return redirect('/produtos/adicionar')
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'produtos/produto_add.html', {'form_produto': form_produto, 'form_categoria': form_categoria})
    else:
        form_produto = FormProduto()
        return render(request, 'produtos/produto_add.html', {'form_produto': form_produto, 'form_categoria': form_categoria})

@login_required
def remover_produto(request, codigo):
    if request.method == 'GET':
        produto = Produto.objects.get(codigo=codigo)
        imagem = Produto.objects.get(codigo=produto.codigo).imagem.name
        if imagem:
            produto.imagem.storage.delete(produto.imagem.name)
        produto.delete()
        return redirect('/produtos')
    else:
        return render(request, 'produtos/produto_list.html')

@login_required
def alterar_produto(request, codigo):
    instance = get_object_or_404(Produto, codigo=codigo)
    produto = Produto.objects.get(codigo=codigo)
    form_produto = FormProduto(request.POST or None, request.FILES or None, instance=instance)
    form_categoria = FormCategoriaProduto()
    if request.method == 'POST':
        if form_produto.is_valid():
            old_img = Produto.objects.get(codigo=produto.codigo).imagem.name
            if not old_img:
                form_produto.save()
            elif form_produto.cleaned_data['imagem'] != old_img:
                produto.imagem.storage.delete(produto.imagem.name)
            form_produto.save()
            messages.add_message(request, messages.SUCCESS, 'Produto alterado!', extra_tags='success')
            return redirect('/produtos')
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'produtos/produto_add.html', {'form_produto': form_produto, 'form_categoria': form_categoria})
    else:
        return render(request, 'produtos/produto_add.html', {'form_produto': form_produto, 'form_categoria': form_categoria})

@login_required
def adicionar_categoria(request):
    if request.method == 'POST':
        form_categoria = FormCategoriaProduto(request.POST)
        if form_categoria.is_valid():
            form_categoria.save()
            messages.add_message(request, messages.SUCCESS, 'Categoria cadastrada!', extra_tags='success')
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
    return redirect('/produtos/adicionar')

@login_required
def gerar_relatorio_pdf(request):
    if request.user.has_perm('produtos.view_produto'):
        buffer = io.BytesIO()
        arquivo = canvas.Canvas(buffer)
        arquivo.setTitle('Gamaware Solution')
        arquivo.drawString(210, 800, f'{datetime.now().strftime("Gerado em %d/%m/%Y às %H:%M")}')
        arquivo.drawString(225, 780, f'Quantidade de produtos: {Produto.objects.all().count()}')
        arquivo.drawString(250, 760, f'Usuário: {request.user.username}')
        margem, linha, ultima_linha, valor_linha, linha_topo = 70, 720, 60, 20, 780
        for produto in Produto.objects.all():
            produto = [
                f'Código: {produto.codigo}',
                f'Produto: {produto.nome}',
                f'Marca: {produto.marca}',
                f'Categoria: {produto.categoria.nome}',
                f'Fornecedor: {produto.fornecedor.nome}',
                f'Valor de custo: R${produto.custo}',
                f'Valor de venda: R${produto.valor}',
                f'Quantidade: {produto.quantidade}',
                f'Link: {produto.link}'
            ]
            for dado in produto:
                arquivo.drawString(margem, linha, dado)
                linha -= valor_linha
                if linha == ultima_linha:
                    arquivo.showPage()
                    linha = linha_topo
            linha -= valor_linha
        arquivo.showPage()
        arquivo.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=False, filename=f'relatorio_produtos_{datetime.now().strftime("%d/%m/%Y")}.pdf')
    return redirect('/')

@login_required
def gerar_relatorio_csv(request):
    if request.user.has_perm('produtos.view_produto'):
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': f'attachment; filename="relatorio_produtos_{datetime.now().strftime("%d/%m/%Y")}.csv"'},
        )
        arquivo = csv.writer(response, delimiter=';')
        arquivo.writerow(['Codigo', 'Produto', 'Quantidade', 'Marca', 'Categoria','Fornecedor', 'Valor de custo', 'Valor de venda', 'Link'])
        for produto in Produto.objects.all():
            arquivo.writerow([
                f'{produto.codigo}',
                f'{produto.nome}',
                f'{produto.quantidade}',
                f'{produto.marca}',
                f'{produto.categoria.nome}',
                f'{produto.fornecedor.nome}',
                f'{produto.custo}',                
                f'{produto.valor}',
                f'{produto.link}'
            ])
        return response
    return redirect('/')