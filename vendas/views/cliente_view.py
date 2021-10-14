from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from vendas.forms import FormCliente
from vendas.models import Clientes

class ClienteListView(LoginRequiredMixin, ListView):
    model = Clientes
    paginate_by = 100
    template_name = 'cliente/cliente_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q') or ''
        object_list = self.model.objects.filter(
            Q(nome__icontains=query) | 
            Q(cpf__icontains=query)
        )
        return object_list

class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Clientes

@login_required
def adicionar_cliente(request):
    if request.method == 'POST':
        form_cliente = FormCliente(request.POST)
        if form_cliente.is_valid():
            if form_cliente.cleaned_data['cpf'] == None or len(form_cliente.cleaned_data['cpf']) == 11:
                if '@' and '.com' in form_cliente.cleaned_data['email']:
                    form_cliente.save()
                    messages.add_message(request, messages.SUCCESS, 'Cliente cadastrado!', extra_tags='success')
                    return redirect('/clientes/adicionar')
                else:
                    messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
                    return render(request, 'cliente/cliente_add.html', {'form': form_cliente})
            else:
                messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
                return render(request, 'cliente/cliente_add.html', {'form': form_cliente})
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'cliente/cliente_add.html', {'form': form_cliente})
    else:
        form_cliente = FormCliente()
        return render(request, 'cliente/cliente_add.html', {'form': form_cliente})

@login_required
def remover_cliente(request, id):
    if request.method == 'GET':
        cliente = Clientes.objects.get(id=id)
        cliente.delete()
        return redirect('/clientes')
    else:
        return render(request, 'cliente/cliente_list.html')

@login_required
def alterar_cliente(request, id): 
    instance = get_object_or_404(Clientes, id=id)
    form_cliente = FormCliente(request.POST or None, instance=instance)
    
    if request.method == 'POST':
        if form_cliente.is_valid():
            form_cliente.save()
            messages.add_message(request, messages.SUCCESS, 'Cliente alterado!', extra_tags='success')
            return redirect('/clientes')
        else:
            messages.add_message(request, messages.ERROR, 'Erro no formulário, tente novamente!', extra_tags='danger')
            return render(request, 'cliente/cliente_add.html', {'form': form_cliente})
    else:
        return render(request, 'cliente/cliente_add.html', {'form': form_cliente})
