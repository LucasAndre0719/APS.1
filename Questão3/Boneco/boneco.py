from enum import Enum


class Direcao(Enum):
    CIMA = "Cima"
    BAIXO = "Baixo"
    DIREITA = "Direita"
    ESQUERDA = "Esquerda"


class BonecoEmMovimento:
    def __init__(self, nome: str, coord_x: float, coord_y: float):
        self.nome = nome
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.direcao_atual = Direcao.CIMA

    def mover_cima(self):
        self.coord_y += 1
        self.direcao_atual = Direcao.CIMA

    def mover_baixo(self):
        self.coord_y -= 1
        self.direcao_atual = Direcao.BAIXO

    def mover_direita(self):
        self.coord_x += 1
        self.direcao_atual = Direcao.DIREITA

    def mover_esquerda(self):
        self.coord_x -= 1
        self.direcao_atual = Direcao.ESQUERDA