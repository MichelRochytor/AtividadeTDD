import unittest
# A classe CalculadoraDesconto ainda não foi criada, o que causará erro
from calculadora import CalculadoraDesconto

class TestCalculadoraDesconto(unittest.TestCase):
    def test_sem_desconto(self):
        calc = CalculadoraDesconto()
        self.assertEqual(calc.calcular(100, "nenhum"), 100) 

    def test_desconto_percentual(self):
        calc = CalculadoraDesconto()
        # Exemplo: 10% de 100 = 90
        self.assertEqual(calc.calcular(100, "percentual", 10), 90) 

    def test_desconto_fixo_cupom(self):
        calc = CalculadoraDesconto()
        # Exemplo: 100 - 20 = 80
        self.assertEqual(calc.calcular(100, "fixo", 20), 80)

    def test_desconto_fixo_nao_negativo(self):
        calc = CalculadoraDesconto()
        # Valor 10 - cupom 20 não deve ser -10, mas sim 0
        self.assertEqual(calc.calcular(10, "fixo", 20), 0)
