from enum import Enum
from datetime import date


class TipoGasto(Enum):
    ROUPA = "Roupa"
    REMEDIO = "Remédio"
    REFEICAO = "Refeição"
    OUTROS = "Outros"


class FormaPagamento(Enum):
    DINHEIRO = "Dinheiro"
    CARTAO_CREDITO = "Cartão de Crédito"
    CARTAO_DEBITO = "Cartão de Débito"
    TICKET_ALIMENTACAO = "Ticket Alimentação"
    VALE_REFEICAO = "Vale Refeição"


class Gasto:
    def __init__(self, tipo: TipoGasto, data: date, valor: float, forma_pagamento: FormaPagamento):
        self.tipo = tipo
        self.data = data
        self.valor = valor
        self.forma_pagamento = forma_pagamento

    def exibir(self):
        return {
            "Tipo": self.tipo.value,
            "Data": self.data.strftime("%d/%m/%Y"),
            "Valor": self.valor,
            "Forma de Pagamento": self.forma_pagamento.value
        }


class ControleGastos:
    def __init__(self):
        self.gastos = []

    def adicionar_gasto(self, gasto: Gasto):
        self.gastos.append(gasto)

    def calcular_total_mensal(self):
        return sum(g.valor for g in self.gastos)

    def agrupar_por_tipo(self):
        agrupado = {}
        for gasto in self.gastos:
            tipo = gasto.tipo.value
            agrupado[tipo] = agrupado.get(tipo, 0) + gasto.valor
        return agrupado

    def total_por_forma_pagamento(self):
        agrupado = {}
        for gasto in self.gastos:
            forma = gasto.forma_pagamento.value
            agrupado[forma] = agrupado.get(forma, 0) + gasto.valor
        return agrupado