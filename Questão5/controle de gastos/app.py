import streamlit as st
import pandas as pd
from datetime import date
from models import TipoDeGasto, FormaPagamento, Gasto, ControleGastos

st.set_page_config(page_title="Controle de Gastos", layout="centered")
st.title("Aplicação - Controle de Gastos")

if "controle" not in st.session_state:
    st.session_state.controle = ControleGastos()

tipo = st.selectbox("Tipo de gasto", [t.name for t in TipoDeGasto])
data_gasto = st.date_input("Data", value=date.today())
valor = st.number_input("Valor", min_value=0.0, format="%.2f")
forma_pagamento = st.selectbox("Forma de pagamento", [f.name for f in FormaPagamento])

if st.button("Adicionar gasto"):
    gasto = Gasto(
        TipoDeGasto[tipo],
        data_gasto,
        valor,
        FormaPagamento[forma_pagamento]
    )
    st.session_state.controle.adicionarGasto(gasto)
    st.success("Gasto cadastrado com sucesso.")

lista = st.session_state.controle.listarGastos()
if lista:
    st.dataframe(pd.DataFrame(lista), use_container_width=True)

st.write("Total do mês:", st.session_state.controle.calcularTotalMensal())