from django.views.generic import ListView
from django.db.models import Q
from produtos.models import Produto

class CatalogoListView(ListView):
    model = Produto
    paginate_by = 100
    template_name = 'produtos/catalogo_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q') or ''
        object_list = self.model.objects.filter(
            Q(nome__icontains=query) |
            Q(marca__icontains=query) | 
            Q(categoria__nome__icontains=query)
        )
        return object_list