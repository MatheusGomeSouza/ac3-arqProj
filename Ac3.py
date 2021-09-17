import abc
from unittest import TestCase, main
import unittest

#operção abc
class Operacao(metaclass=abc.ABCMeta):
    def executar(self, valor1, valor2):
        pass

#operações
class OperacaoFabrica(object):
    def criar(self, operador):
        if operador == 'soma':
            return Soma()
        if operador == 'subtracao':
            return Subtracao()
        if operador == 'divisao':
            return Divisao()
        if operador == 'multiplicação':
            return Multiplicacao()

class Calculadora(object):
    def calcular (self, valor1, valor2, operador):
        OperacaoFabricacl = OperacaoFabrica()
        operacao = OperacaoFabricacl.criar(operador)
        if(operacao == None):
            return 0
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado


#operações
class Soma(Operacao):
    def executar(self, valor1, valor2):
        return valor1 + valor2

class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 - valor2

class Divisao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 / valor2

class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 * valor2


# testes
class Testes(unittest.TestCase):
    def test_soma(self):
        calculadorSoma = Calculadora()
        self.assertEqual(calculadorSoma.calcular(2, 3, 'soma'), 5)

    def test_multiplicacao(self):
        calculadorMultiplicacao = Calculadora()
        self.assertEqual(calculadorMultiplicacao.calcular(2, 5, 'multiplicação'), 10)

    def test_divisao(self):
        calculadorDivisao = Calculadora()
        self.assertEqual(calculadorDivisao.calcular(2, 4, 'divisao'), 0.5)

    def test_subtracao(self):
        calculadorSubtracao = Calculadora()
        self.assertEqual(calculadorSubtracao.calcular(4,2, 'subtracao'),2)


if __name__ == '__main__':
    unittest.main()