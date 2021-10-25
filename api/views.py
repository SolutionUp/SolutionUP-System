from produtos.models import Produto 
from django.http import JsonResponse

def get_produto(request, codigo):
    if request.method != 'GET':
        return JsonResponse({"error": "method not allowed"})

    try:
        produto = Produto.objects.get(codigo=codigo)
        return JsonResponse({"qtd": produto.quantidade})
    except:
        return JsonResponse({"qtd": 0 })
