from item_comanda import ItemComanda
from produto import Produto


class Comanda:
    def __init__(self, numero: int):
        self.numero = numero
        self.itens = []
        self.total = 0.0

    def registrar_produto(self, produto: Produto, quantidade: int):
        item = ItemComanda(produto, quantidade)
        self.itens.append(item)
        self.calcular_total()

    def exibir_comanda(self):
        return self.itens

    def calcular_total(self) -> float:
        self.total = sum(item.subtotal for item in self.itens)
        return self.total

    def finalizar_compra(self):
        return f"Compra finalizada. Total da comanda: R$ {self.total:.2f}"