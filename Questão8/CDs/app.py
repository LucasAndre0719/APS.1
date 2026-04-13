import streamlit as st
import pandas as pd


class CD:
    def __init__(self, cantorOuConjunto: str, titulo: str, anoLancamento: int):
        self.cantorOuConjunto = cantorOuConjunto
        self.titulo = titulo
        self.anoLancamento = anoLancamento

    def cadastrar(self):
        return "CD cadastrado com sucesso."

    def exibir(self):
        return {
            "Cantor ou Conjunto": self.cantorOuConjunto,
            "Título": self.titulo,
            "Ano de Lançamento": self.anoLancamento
        }


class ColecaoCD:
    def __init__(self):
        self.cds = []

    def adicionarCD(self, cd: CD):
        self.cds.append(cd)

    def listarCDs(self):
        return [cd.exibir() for cd in self.cds]

    def buscarPorTitulo(self, titulo: str):
        for cd in self.cds:
            if cd.titulo.lower() == titulo.lower():
                return cd
        return None

    def buscarPorCantor(self, nome: str):
        return [cd for cd in self.cds if nome.lower() in cd.cantorOuConjunto.lower()]


st.set_page_config(page_title="Coleção de CDs", layout="centered")
st.title("Aplicação - Coleção de CDs")

if "colecao" not in st.session_state:
    st.session_state.colecao = ColecaoCD()

st.subheader("Cadastrar CD")

cantor = st.text_input("Cantor ou Conjunto")
titulo = st.text_input("Título do CD")
ano = st.number_input("Ano de lançamento", min_value=1900, max_value=2100, value=2024)

if st.button("Adicionar CD"):
    cd = CD(cantorOuConjunto=cantor, titulo=titulo, anoLancamento=int(ano))
    st.session_state.colecao.adicionarCD(cd)
    st.success(cd.cadastrar())

st.markdown("---")
st.subheader("Lista de CDs")

lista_cds = st.session_state.colecao.listarCDs()

if lista_cds:
    df = pd.DataFrame(lista_cds)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Nenhum CD cadastrado.")

st.markdown("---")
st.subheader("Buscar por título")

titulo_busca = st.text_input("Digite o título para buscar")

if st.button("Buscar título"):
    resultado = st.session_state.colecao.buscarPorTitulo(titulo_busca)
    if resultado:
        st.success("CD encontrado!")
        st.write(resultado.exibir())
    else:
        st.warning("Nenhum CD encontrado com esse título.")

st.markdown("---")
st.subheader("Buscar por cantor ou conjunto")

cantor_busca = st.text_input("Digite o cantor ou conjunto")

if st.button("Buscar cantor"):
    resultados = st.session_state.colecao.buscarPorCantor(cantor_busca)
    if resultados:
        dados = [cd.exibir() for cd in resultados]
        df_resultado = pd.DataFrame(dados)
        st.dataframe(df_resultado, use_container_width=True)
    else:
        st.warning("Nenhum CD encontrado para esse cantor ou conjunto.")