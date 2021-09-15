from django.test import TestCase

from produtos.models import CategoriaProduto, Produto, Fornecedor

class CategoriaProdutoTestCase(TestCase):
    def setUp(self):
        CategoriaProduto.objects.create(
            nome='Categoria A'
        )
    
    def test_categoria_criada(self):
        categoria_produto = CategoriaProduto.objects.get()
        self.assertEqual(categoria_produto.nome, 'Categoria A')

class ProdutoTestCase(TestCase):
    def setUp(self):
        Fornecedor.objects.create(
            nome='Fornecedor A',
            ramo='Loja de Informática',
            email='fornecedor@exemplo.com.br',
            telefone='1140042020',
            celular='11940042020'
        )
        CategoriaProduto.objects.create(
            nome='Categoria A'
        )
        Produto.objects.create(
            nome='Produto A',
            valor=100.00,
            descricao='Descrição exemplo do Produto A',
            marca='Marca A',
            link='https://www.mercadolivre.com.br/produto-a',
            fornecedor=Fornecedor.objects.get(nome='Fornecedor A'),
            categoria=CategoriaProduto.objects.get(nome='Categoria A')
        )

    def test_produto_criado(self):
        produto = Produto.objects.get()
        self.assertEqual(produto.nome, 'Produto A')

    def test_produto_com_valor(self):
        produto = Produto.objects.get()
        self.assertEqual(produto.valor, 100.00)

    def test_produto_com_descricao(self):
        produto = Produto.objects.get()
        self.assertEqual(produto.descricao, 'Descrição exemplo do Produto A')
        
    def test_produto_com_marca(self):
        produto = Produto.objects.get()
        self.assertEqual(produto.marca, 'Marca A')

    def test_produto_com_link(self):
        produto = Produto.objects.get()
        self.assertEqual(produto.link, 'https://www.mercadolivre.com.br/produto-a')

    def test_produto_com_fornecedor(self):
        produto = Produto.objects.get()
        self.assertEqual(produto.fornecedor.nome, 'Fornecedor A')

    def test_produto_com_categoria(self):
        produto = Produto.objects.get()
        self.assertEqual(produto.categoria.nome, 'Categoria A')

class FornecedorTestCase(TestCase):
    def setUp(self):
        Fornecedor.objects.create(
            nome='Fornecedor A',
            ramo='Loja de Informática',
            email='fornecedor@exemplo.com.br',
            telefone='1140042020',
            celular='11940042020'
        )

    def test_fornecedor_criado(self):
        fornecedor = Fornecedor.objects.get()
        self.assertEqual(fornecedor.nome, 'Fornecedor A')

    def test_fornecedor_com_ramo(self):
        fornecedor = Fornecedor.objects.get()
        self.assertEqual(fornecedor.ramo, 'Loja de Informática')

    def test_fornecedor_com_email(self):
        fornecedor = Fornecedor.objects.get()
        self.assertEqual(fornecedor.email, 'fornecedor@exemplo.com.br')
        
    def test_fornecedor_com_telefone(self):
        fornecedor = Fornecedor.objects.get()
        self.assertEqual(fornecedor.telefone, '1140042020')

    def test_fornecedor_com_celular(self):
        fornecedor = Fornecedor.objects.get()
        self.assertEqual(fornecedor.celular, '11940042020')
