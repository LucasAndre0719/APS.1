class Produto:
    def __init__(self, nome: str, valor_unitario: float):
        self.nome = nome
        self.valor_unitario = valor_unitario

    def exibir_produto(self) -> str:
        return f"{self.nome} - R$ {self.valor_unitario:.2f}"