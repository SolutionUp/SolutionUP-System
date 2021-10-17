from django.urls import path, include
from produtos.views.catalogo_view import *

urlpatterns = [
    path('', CatalogoListView.as_view(), name='listagem_catalogo')
]