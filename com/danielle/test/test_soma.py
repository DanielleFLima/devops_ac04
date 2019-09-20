from unittest import TestCase
from com.danielle.soma import Soma


class TestSoma(TestCase):

	def setUp(self):
		self.soma = Soma()
		
	def test_soma(self):
		self.assertEqual(self.soma.soma_10(5), 15, "Should be 15")