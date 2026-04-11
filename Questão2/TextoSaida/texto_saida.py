from enum import Enum


class Cor(Enum):
    PRETO = "preto"
    BRANCO = "branco"
    AZUL = "azul"
    AMARELO = "amarelo"
    CINZA = "cinza"


class TipoComponente(Enum):
    LABEL = "label"
    EDIT = "edit"
    MEMO = "memo"


class TextoSaida:
    def __init__(self, texto: str, tamanho_fonte: int,
                 cor_fonte: Cor, cor_fundo: Cor,
                 tipo_componente: TipoComponente):
        self.texto = texto
        self.tamanho_fonte = tamanho_fonte
        self.cor_fonte = cor_fonte
        self.cor_fundo = cor_fundo
        self.tipo_componente = tipo_componente

    def _mapear_cor_html(self, cor: Cor) -> str:
        mapa = {
            Cor.PRETO: "black",
            Cor.BRANCO: "white",
            Cor.AZUL: "blue",
            Cor.AMARELO: "yellow",
            Cor.CINZA: "gray"
        }
        return mapa[cor]

    def exibir(self) -> str:
        cor_texto = self._mapear_cor_html(self.cor_fonte)
        cor_fundo = self._mapear_cor_html(self.cor_fundo)

        estilo = f"""
        color: {cor_texto};
        background-color: {cor_fundo};
        font-size: {self.tamanho_fonte}px;
        padding: 10px;
        border-radius: 8px;
        margin-top: 10px;
        """

        if self.tipo_componente == TipoComponente.LABEL:
            return f"<div style='{estilo}'>{self.texto}</div>"

        elif self.tipo_componente == TipoComponente.EDIT:
            return f"""
            <input
                type='text'
                value='{self.texto}'
                style='{estilo} width: 100%; border: 1px solid #ccc;'
            />
            """

        elif self.tipo_componente == TipoComponente.MEMO:
            return f"""
            <textarea
                rows='6'
                style='{estilo} width: 100%; border: 1px solid #ccc;'
            >{self.texto}</textarea>
            """

        return f"<div style='{estilo}'>{self.texto}</div>"