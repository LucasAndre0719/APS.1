from enum import Enum
from datetime import date


class TipoDeGasto(Enum):
    ROUPAS = "ROUPAS"
    REMEDIO = "REMEDIO"
    ALIMENTACAO = "ALIMENTACAO"


class FormaPagamento(Enum):
    DINHEIRO = "DINHEIRO"
    CARTAO_CREDITO = "CARTAO_CREDITO"
    CARTAO_DEBITO = "CARTAO_DEBITO"
    TICKET_ALIMENTACAO = "TICKET_ALIMENTACAO"
    VALE_REFEICAO = "VALE_REFEICAO"


class Gasto:
    def __init__(self, tipo, data, valor, formaPagamento):
        self.tipo = tipo
        self.data = data
        self.valor = valor
        self.formaPagamento = formaPagamento

    def cadastrar(self):
        return "Gasto cadastrado com sucesso."

    def exibir(self):
        return {
            "Tipo": self.tipo.value,
            "Data": self.data.strftime("%d/%m/%Y"),
            "Valor": self.valor,
            "Forma de Pagamento": self.formaPagamento.value
        }


class ControleGastos:
    def __init__(self):
        self.gastos = []

    def adicionarGasto(self, g):
        self.gastos.append(g)

    def calcularTotalMensal(self):
        hoje = date.today()
        total = 0
        for gasto in self.gastos:
            if gasto.data.month == hoje.month and gasto.data.year == hoje.year:
                total += gasto.valor
        return total

    def agruparPorTipo(self):
        agrupado = {}
        for gasto in self.gastos:
            tipo = gasto.tipo.value
            agrupado[tipo] = agrupado.get(tipo, 0) + gasto.valor
        return agrupado

    def totalPorFormaPagamento(self):
        agrupado = {}
        for gasto in self.gastos:
            forma = gasto.formaPagamento.value
            agrupado[forma] = agrupado.get(forma, 0) + gasto.valor
        return agrupado

    def listarGastos(self):
        return [g.exibir() for g in self.gastos]