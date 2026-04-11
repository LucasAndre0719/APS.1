import streamlit as st
import pandas as pd
from datetime import date
from gasto_luz import GastoDeLuz
from controle_gastos import ControleGastos

st.set_page_config(page_title="Conta de Luz", page_icon="💡")
st.title("Lista de Acompanhamento de Gasto de Luz")

# Inicializa lista na sessão
if "contas" not in st.session_state:
    st.session_state.contas = []

st.subheader("Cadastrar nova conta")

with st.form("form_conta"):
    col1, col2 = st.columns(2)

    with col1:
        data_leitura = st.date_input("Data da leitura", value=date.today())
        numero_leitura = st.number_input("Nº da leitura", min_value=0, step=1)
        kw_gasto = st.number_input("KW gasto", min_value=0.0, step=0.1)

    with col2:
        valor_a_pagar = st.number_input("Valor a pagar (R$)", min_value=0.0, step=0.01)
        data_pagamento = st.date_input("Data do pagamento", value=date.today())

    adicionar = st.form_submit_button("Adicionar")

if adicionar:
    nova = GastoDeLuz(
        data_leitura=data_leitura,
        numero_leitura=int(numero_leitura),
        kw_gasto=kw_gasto,
        valor_a_pagar=valor_a_pagar,
        data_pagamento=data_pagamento
    )
    st.session_state.contas.append(nova)
    st.success("Conta cadastrada!")

if st.session_state.contas:
    st.subheader("Registros")

    dados = [{
        "Data Leitura": g.data_leitura.strftime("%d/%m/%Y"),
        "Nº Leitura": g.numero_leitura,
        "KW Gasto": g.kw_gasto,
        "Valor a Pagar": f"R$ {g.valor_a_pagar:.2f}",
        "Data Pagamento": g.data_pagamento.strftime("%d/%m/%Y"),
        "Média Consumo": g.media_consumo,
    } for g in st.session_state.contas]

    st.dataframe(pd.DataFrame(dados), use_container_width=True)

    controle = ControleGastos()
    controle.contas = st.session_state.contas

    menor = controle.menor_consumo()
    maior = controle.maior_consumo()

    st.subheader("Pesquisas mensais")
    col1, col2 = st.columns(2)

    col1.metric(
        "Menor consumo",
        f"{menor.kw_gasto} KW",
        menor.data_leitura.strftime("%b/%y")
    )

    col2.metric(
        "Maior consumo",
        f"{maior.kw_gasto} KW",
        maior.data_leitura.strftime("%b/%y")
    )