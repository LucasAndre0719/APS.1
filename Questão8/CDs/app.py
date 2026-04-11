import streamlit as st
import pandas as pd
from cd import CD, ColecaoCD

st.set_page_config(page_title="Coleção de CDs", page_icon="💿")
st.title("Coleção de CDs")

if "colecao" not in st.session_state:
    st.session_state.colecao = ColecaoCD()

colecao = st.session_state.colecao

st.subheader("Cadastrar CD")

with st.form("form_cd"):
    cantor = st.text_input("Cantor(a) ou conjunto")
    titulo = st.text_input("Título do CD")
    ano = st.number_input("Ano de lançamento", min_value=1900, max_value=2100, step=1)

    cadastrar = st.form_submit_button("Cadastrar CD")

if cadastrar:
    if cantor.strip() == "" or titulo.strip() == "":
        st.warning("Preencha cantor/conjunto e título.")
    else:
        novo_cd = CD(cantor, titulo, int(ano))
        colecao.adicionar_cd(novo_cd)
        st.success("CD cadastrado com sucesso!")

if colecao.cds:
    st.subheader("Lista de CDs")

    dados = colecao.listar_cds()
    df = pd.DataFrame(dados)
    st.dataframe(df, use_container_width=True)

    st.subheader("Buscar por título")
    titulo_busca = st.text_input("Digite o título exato", key="busca_titulo")

    if st.button("Buscar título"):
        resultado = colecao.buscar_por_titulo(titulo_busca)
        if resultado:
            st.success("CD encontrado!")
            st.write(resultado.exibir())
        else:
            st.warning("Nenhum CD encontrado com esse título.")

    st.subheader("Buscar por cantor/conjunto")
    cantor_busca = st.text_input("Digite o nome do cantor ou conjunto", key="busca_cantor")

    if st.button("Buscar cantor/conjunto"):
        resultados = colecao.buscar_por_cantor(cantor_busca)
        if resultados:
            st.success(f"{len(resultados)} CD(s) encontrado(s).")
            st.dataframe(
                pd.DataFrame([cd.exibir() for cd in resultados]),
                use_container_width=True
            )
        else:
            st.warning("Nenhum CD encontrado para esse cantor/conjunto.")