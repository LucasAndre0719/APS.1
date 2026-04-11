from produto_compra import ProdutoCompra


class ListaCompra:
    def __init__(self):
        self.itens = []
        self.total = 0.0

    def adicionar_produto(self, produto: ProdutoCompra):
        self.itens.append(produto)
        self.calcular_total()

    def calcular_total(self) -> float:
        self.total = sum(item.calcular_subtotal() for item in self.itens)
        return self.total

    def listar_produtos(self):
        return [item.exibir() for item in self.itens]

    def atualizar_preco_produto(self, nome_produto: str, novo_preco: float):
        for item in self.itens:
            if item.nome == nome_produto:
                item.atualizar_preco(novo_preco)
                break
        self.calcular_total()

    def atualizar_quantidade_produto(self, nome_produto: str, nova_qtd: float):
        for item in self.itens:
            if item.nome == nome_produto:
                item.qtd_compra = nova_qtd
                item.calcular_subtotal()
                break
        self.calcular_total()

    def excluir_produto(self, nome_produto: str):
        self.itens = [item for item in self.itens if item.nome != nome_produto]
        self.calcular_total()