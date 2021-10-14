from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from produtos.forms import FormFornecedor
from produtos.models import Fornecedor


class FornecedorListView(LoginRequiredMixin, ListView):
    model = Fornecedor
    paginate_by = 100
    template_name = 'fornecedor/fornecedor_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q') or ''
        object_list = self.model.objects.filter(
            Q(nome__icontains=query) | 
            Q(ramo__icontains=query)
        )
        return object_list


class FornecedorDetailView(LoginRequiredMixin, DetailView):
    model = Fornecedor

@login_required
def adicionar_fornecedor(request):
    if request.method == 'POST':
        form_fornecedor = FormFornecedor(request.POST)
        if form_fornecedor.is_valid():
            if '@' and '.com' in form_fornecedor.cleaned_data['email']:
                form_fornecedor.save()
                messages.add_message(request, messages.SUCCESS, 'Fornecedor cadastrado!', extra_tags='success')
                return redirect('/fornecedores/adicionar')
            else:
                messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
                return render(request, 'fornecedor/fornecedor_add.html', {'form': form_fornecedor})
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'fornecedor/fornecedor_add.html', {'form': form_fornecedor})
    else:
        form_fornecedor = FormFornecedor()
        return render(request, 'fornecedor/fornecedor_add.html', {'form': form_fornecedor})

@login_required
def remover_fornecedor(request, id):
    if request.method == 'GET':
        fornecedor = Fornecedor.objects.get(id=id)
        fornecedor.delete()
        return redirect('/fornecedores')
    else:
        return render(request, 'fornecedor/fornecedor_list.html')

@login_required
def alterar_fornecedor(request, id): 
    instance = get_object_or_404(Fornecedor, id=id)
    form_fornecedor = FormFornecedor(request.POST or None, instance=instance)
    
    if request.method == 'POST':
        if form_fornecedor.is_valid():
            form_fornecedor.save()
            messages.add_message(request, messages.SUCCESS, 'Fornecedor alterado!', extra_tags='success')
            return redirect('/fornecedores')
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'fornecedor/fornecedor_add.html', {'form': form_fornecedor})
    else:
        return render(request, 'fornecedor/fornecedor_add.html', {'form': form_fornecedor})
