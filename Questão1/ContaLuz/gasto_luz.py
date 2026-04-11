from datetime import date


class GastoDeLuz:
    def __init__(self, data_leitura: date, numero_leitura: int,
                 kw_gasto: float, valor_a_pagar: float,
                 data_pagamento: date):
        self.data_leitura = data_leitura
        self.numero_leitura = numero_leitura
        self.kw_gasto = kw_gasto
        self.valor_a_pagar = valor_a_pagar
        self.data_pagamento = data_pagamento
        self.media_consumo = self.calcular_media_consumo()

    def calcular_media_consumo(self) -> float:
        return round(self.kw_gasto / 30, 2)