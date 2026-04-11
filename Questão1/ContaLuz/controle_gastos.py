from gasto_luz import GastoDeLuz


class ControleGastos:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta: GastoDeLuz):
        self.contas.append(conta)

    def menor_consumo(self) -> GastoDeLuz | None:
        if not self.contas:
            return None
        return min(self.contas, key=lambda g: g.kw_gasto)

    def maior_consumo(self) -> GastoDeLuz | None:
        if not self.contas:
            return None
        return max(self.contas, key=lambda g: g.kw_gasto)
    