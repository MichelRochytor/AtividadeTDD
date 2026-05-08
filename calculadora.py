from abc import ABC, abstractmethod

class PoliticaDesconto(ABC):
    @abstractmethod
    def calcular(self, valor, extra=0):
        pass

class SemDesconto(PoliticaDesconto):
    def calcular(self, valor, extra=0):
        return valor

class DescontoPercentual(PoliticaDesconto):
    def calcular(self, valor, extra=0):
        return valor * (1 - extra / 100)

class DescontoFixo(PoliticaDesconto):
    def calcular(self, valor, extra=0):
        return max(0, valor - extra)

# Contexto que utiliza a Strategy
class CalculadoraDesconto:
    def __init__(self):
        self.estrategias = {
            "nenhum": SemDesconto(),
            "percentual": DescontoPercentual(),
            "fixo": DescontoFixo()
        }

    def calcular(self, valor, tipo, extra=0):
        estrategia = self.estrategias.get(tipo, SemDesconto())
        return estrategia.calcular(valor, extra)