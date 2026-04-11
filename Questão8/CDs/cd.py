class CD:
    def __init__(self, cantor_ou_conjunto: str, titulo: str, ano_lancamento: int):
        self.cantor_ou_conjunto = cantor_ou_conjunto
        self.titulo = titulo
        self.ano_lancamento = ano_lancamento

    def exibir(self):
        return {
            "Cantor/Conjunto": self.cantor_ou_conjunto,
            "Título": self.titulo,
            "Ano de Lançamento": self.ano_lancamento
        }


class ColecaoCD:
    def __init__(self):
        self.cds = []

    def adicionar_cd(self, cd: CD):
        self.cds.append(cd)

    def listar_cds(self):
        return [cd.exibir() for cd in self.cds]

    def buscar_por_titulo(self, titulo: str):
        for cd in self.cds:
            if cd.titulo.lower() == titulo.lower():
                return cd
        return None

    def buscar_por_cantor(self, nome: str):
        resultados = []
        for cd in self.cds:
            if nome.lower() in cd.cantor_ou_conjunto.lower():
                resultados.append(cd)
        return resultados