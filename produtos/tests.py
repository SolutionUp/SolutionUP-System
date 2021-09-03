from django.test import TestCase

from produtos.models import Produto, Fornecedor

class ProdutoTestCase(TestCase):
    def setUp(self):
        pass

    def test_produto_criado(self):
        Produto.objects.create(
            nome='ProdutoA',
            valor=100.00
        )
        p = Produto.objects.get(nome='ProdutoA')
        self.assertEqual(p.nome, 'ProdutoA')

class FornecedorTestCase(TestCase):
    def setUp(self):
        pass

    def test_fornecedor_criado(self):
        Fornecedor.objects.create(
            nome='FornecedorA',
            email='teste@teste.com',
            ramo='Notebooks'
        )
        p = Fornecedor.objects.get(nome='FornecedorA')
        self.assertEqual(p.nome, 'FornecedorA')
