class ProdutoCompra:
    def __init__(self, nome: str, unidade_compra: str, qtd_mes: float, qtd_compra: float, preco_estimado: float):
        self.nome = nome
        self.unidade_compra = unidade_compra
        self.qtd_mes = qtd_mes
        self.qtd_compra = qtd_compra
        self.preco_estimado = preco_estimado
        self.subtotal = self.calcular_subtotal()

    def calcular_subtotal(self) -> float:
        self.subtotal = self.qtd_compra * self.preco_estimado
        return self.subtotal

    def atualizar_preco(self, novo_preco: float):
        self.preco_estimado = novo_preco
        self.calcular_subtotal()

    def exibir(self):
        return {
            "Produto": self.nome,
            "Unidade": self.unidade_compra,
            "Qtd. Mês": self.qtd_mes,
            "Qtd. Compra": self.qtd_compra,
            "Preço Estimado": self.preco_estimado,
            "Subtotal": self.subtotal
        }