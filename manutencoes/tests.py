from django.test import TestCase

from manutencoes.models import Terceiro

class TerceiroTestCase(TestCase):
    def setUp(self):
        Terceiro.objects.create(
            nome='Terceiro A',
            ramo='Manutenção de Notebooks',
            email='terceiro@exemplo.com.br',
            telefone='1150052020',
            celular='11950052020'
        )

    def test_terceiro_criado(self):
        terceiro = Terceiro.objects.get()
        self.assertEqual(terceiro.nome, 'Terceiro A')

    def test_terceiro_com_ramo(self):
        terceiro = Terceiro.objects.get()
        self.assertEqual(terceiro.ramo, 'Manutenção de Notebooks')

    def test_terceiro_com_email(self):
        terceiro = Terceiro.objects.get()
        self.assertEqual(terceiro.email, 'terceiro@exemplo.com.br')
        
    def test_terceiro_com_telefone(self):
        terceiro = Terceiro.objects.get()
        self.assertEqual(terceiro.telefone, '1150052020')

    def test_terceiro_com_celular(self):
        terceiro = Terceiro.objects.get()
        self.assertEqual(terceiro.celular, '11950052020')
