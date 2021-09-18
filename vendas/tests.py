from django.test import TestCase

from vendas.models import Clientes

class ClientesTestCase(TestCase):
    def setUp(self):
        Clientes.objects.create(
            nome='Cliente A',
            cpf='12345678910',
            email='cliente@exemplo.com.br',
            telefone='1160062020',
            celular='11960062020'
        )
    
    def test_cliente_criado(self):
        cliente = Clientes.objects.get()
        self.assertEqual(cliente.nome, 'Cliente A')

    def test_cliente_com_cpf(self):
        cliente = Clientes.objects.get()
        self.assertEqual(cliente.cpf, '12345678910')

    def test_cliente_com_email(self):
        cliente = Clientes.objects.get()
        self.assertEqual(cliente.email, 'cliente@exemplo.com.br')
        
    def test_cliente_com_telefone(self):
        cliente = Clientes.objects.get()
        self.assertEqual(cliente.telefone, '1160062020')

    def test_cliente_com_celular(self):
        cliente = Clientes.objects.get()
        self.assertEqual(cliente.celular, '11960062020')
