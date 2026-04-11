import streamlit as st
import pandas as pd
from produto import Produto
from comanda import Comanda

st.set_page_config(page_title="Comanda Eletrônica", page_icon="🧾")
st.title("Comanda Eletrônica (PDV)")

# Estado da sessão
if "produtos" not in st.session_state:
    st.session_state.produtos = []

if "comanda" not in st.session_state:
    st.session_state.comanda = Comanda(numero=1)

# Cadastro de produtos
st.subheader("Cadastrar Produto")

with st.form("form_produto"):
    nome_produto = st.text_input("Nome do produto")
    valor_unitario = st.number_input("Valor unitário", min_value=0.0, step=0.01)
    cadastrar_produto = st.form_submit_button("Cadastrar produto")

if cadastrar_produto:
    if nome_produto.strip() == "":
        st.warning("Informe o nome do produto.")
    else:
        novo_produto = Produto(nome_produto, valor_unitario)
        st.session_state.produtos.append(novo_produto)
        st.success("Produto cadastrado com sucesso!")

# Mostrar produtos cadastrados
if st.session_state.produtos:
    st.subheader("Produtos cadastrados")

    dados_produtos = [
        {
            "Nome": p.nome,
            "Valor Unitário": f"R$ {p.valor_unitario:.2f}"
        }
        for p in st.session_state.produtos
    ]

    st.dataframe(pd.DataFrame(dados_produtos), use_container_width=True)

# Registrar item na comanda
if st.session_state.produtos:
    st.subheader("Registrar Produto na Comanda")

    nomes_produtos = [p.nome for p in st.session_state.produtos]

    with st.form("form_item"):
        nome_escolhido = st.selectbox("Selecione o produto", nomes_produtos)
        quantidade = st.number_input("Quantidade", min_value=1, step=1)
        adicionar_item = st.form_submit_button("Adicionar à comanda")

    if adicionar_item:
        produto_escolhido = next(
            (p for p in st.session_state.produtos if p.nome == nome_escolhido),
            None
        )

        if produto_escolhido:
            st.session_state.comanda.registrar_produto(produto_escolhido, quantidade)
            st.success("Produto adicionado à comanda!")

# Exibir comanda
if st.session_state.comanda.itens:
    st.subheader(f"Comanda Nº {st.session_state.comanda.numero}")

    dados_itens = []
    for item in st.session_state.comanda.exibir_comanda():
        dados_itens.append({
            "Produto": item.produto.nome,
            "Quantidade": item.quantidade,
            "Valor Unitário": f"R$ {item.produto.valor_unitario:.2f}",
            "Subtotal": f"R$ {item.subtotal:.2f}"
        })

    st.dataframe(pd.DataFrame(dados_itens), use_container_width=True)

    total = st.session_state.comanda.calcular_total()
    st.metric("Total da Comanda", f"R$ {total:.2f}")

    if st.button("Finalizar compra"):
        mensagem = st.session_state.comanda.finalizar_compra()
        st.success(mensagem)