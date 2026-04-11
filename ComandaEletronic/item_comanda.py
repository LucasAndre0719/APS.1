from produto import Produto


class ItemComanda:
    def __init__(self, produto: Produto, quantidade: int):
        self.quantidade = quantidade
        self.produto = produto
        self.subtotal = self.calcular_subtotal()

    def calcular_subtotal(self) -> float:
        return self.quantidade * self.produto.valor_unitario