from enum import Enum


class COR(Enum):
    preto = "black"
    branco = "white"
    azul = "blue"
    amarelo = "yellow"
    cinza = "gray"


class TipoComponente(Enum):
    label = "label"
    edit = "edit"
    memo = "memo"


class TextoSaida:
    def __init__(self, tamanhoFonte: int, cor_fonte: COR, cor_fundo: COR, texto: str, tipoComponente: TipoComponente):
        self.tamanhoFonte = tamanhoFonte
        self.cor_fonte = cor_fonte
        self.cor_fundo = cor_fundo
        self.texto = texto
        self.tipoComponente = tipoComponente