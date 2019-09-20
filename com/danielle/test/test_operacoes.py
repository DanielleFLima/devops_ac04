from unittest import TestCase
fromm com.danielle.operacoes import operacoes


class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Operacoes()
		
	def test_soma(self):
		self.assertEqual(self.operacoes.soma([1,5]), 6, "Should be 6")