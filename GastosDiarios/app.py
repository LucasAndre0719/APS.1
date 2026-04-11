import streamlit as st
import pandas as pd
from datetime import date
from gasto import Gasto, ControleGastos, TipoGasto, FormaPagamento

st.set_page_config(page_title="Gastos Diários", page_icon="💸")
st.title("Controle de Gastos Diários")

if "gastos" not in st.session_state:
    st.session_state.gastos = []

st.subheader("Cadastrar novo gasto")

with st.form("form_gasto"):
    tipo = st.selectbox("Tipo do gasto", [t.value for t in TipoGasto])
    data_gasto = st.date_input("Data do gasto", value=date.today())
    valor = st.number_input("Valor do gasto", min_value=0.0, step=0.01)
    forma_pagamento = st.selectbox("Forma de pagamento", [f.value for f in FormaPagamento])

    adicionar = st.form_submit_button("Adicionar gasto")

if adicionar:
    novo_gasto = Gasto(
        tipo=TipoGasto(tipo),
        data=data_gasto,
        valor=valor,
        forma_pagamento=FormaPagamento(forma_pagamento)
    )
    st.session_state.gastos.append(novo_gasto)
    st.success("Gasto cadastrado com sucesso!")

if st.session_state.gastos:
    controle = ControleGastos()
    controle.gastos = st.session_state.gastos

    st.subheader("Lista de gastos")

    dados = [g.exibir() for g in st.session_state.gastos]
    df = pd.DataFrame(dados)
    df["Valor"] = df["Valor"].map(lambda x: f"R$ {x:.2f}")
    st.dataframe(df, use_container_width=True)

    st.subheader("Resumo do mês")

    total_mensal = controle.calcular_total_mensal()
    st.metric("Total mensal", f"R$ {total_mensal:.2f}")

    st.subheader("Total por tipo de gasto")
    por_tipo = controle.agrupar_por_tipo()
    df_tipo = pd.DataFrame(
        [{"Tipo": k, "Total": v} for k, v in por_tipo.items()]
    )
    if not df_tipo.empty:
        df_tipo["Total"] = df_tipo["Total"].map(lambda x: f"R$ {x:.2f}")
        st.dataframe(df_tipo, use_container_width=True)

    st.subheader("Total por forma de pagamento")
    por_forma = controle.total_por_forma_pagamento()
    df_forma = pd.DataFrame(
        [{"Forma de Pagamento": k, "Total": v} for k, v in por_forma.items()]
    )
    if not df_forma.empty:
        df_forma["Total"] = df_forma["Total"].map(lambda x: f"R$ {x:.2f}")
        st.dataframe(df_forma, use_container_width=True)

        