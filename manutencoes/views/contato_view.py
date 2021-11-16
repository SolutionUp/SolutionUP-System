from django.views.generic import ListView
from django.shortcuts import render


def ContatoListView(request):
    return render(request,"chamado/contato_list.html")