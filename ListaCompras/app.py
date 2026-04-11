import streamlit as st
import pandas as pd
from produto_compra import ProdutoCompra
from lista_compra import ListaCompra

st.set_page_config(page_title="Lista de Compras", page_icon="🛒")
st.title("Lista de Compras Mensal")

if "lista_compra" not in st.session_state:
    st.session_state.lista_compra = ListaCompra()

lista = st.session_state.lista_compra

st.subheader("Cadastrar produto")

with st.form("form_produto"):
    nome = st.text_input("Nome do produto")
    unidade_compra = st.text_input("Unidade de compra", value="Kg")
    qtd_mes = st.number_input("Quantidade prevista para o mês", min_value=0.0, step=0.5)
    qtd_compra = st.number_input("Quantidade efetivamente comprada", min_value=0.0, step=0.5)
    preco_estimado = st.number_input("Preço estimado", min_value=0.0, step=0.01)

    adicionar = st.form_submit_button("Adicionar produto")

if adicionar:
    if nome.strip() == "":
        st.warning("Informe o nome do produto.")
    else:
        produto = ProdutoCompra(
            nome=nome,
            unidade_compra=unidade_compra,
            qtd_mes=qtd_mes,
            qtd_compra=qtd_compra,
            preco_estimado=preco_estimado
        )
        lista.adicionar_produto(produto)
        st.success("Produto adicionado com sucesso!")

if lista.itens:
    st.subheader("Produtos cadastrados")

    dados = lista.listar_produtos()
    df = pd.DataFrame(dados)

    df["Preço Estimado"] = df["Preço Estimado"].map(lambda x: f"R$ {x:.2f}")
    df["Subtotal"] = df["Subtotal"].map(lambda x: f"R$ {x:.2f}")

    st.dataframe(df, use_container_width=True)

    st.metric("Total da compra", f"R$ {lista.calcular_total():.2f}")

    nomes_produtos = [item.nome for item in lista.itens]

    st.subheader("Editar quantidade comprada")

    col1, col2 = st.columns(2)

    with col1:
        produto_qtd = st.selectbox("Selecione o produto para editar", nomes_produtos, key="editar_qtd_prod")
    with col2:
        nova_qtd = st.number_input("Nova quantidade comprada", min_value=0.0, step=0.5, key="nova_qtd")

    if st.button("Atualizar quantidade"):
        lista.atualizar_quantidade_produto(produto_qtd, nova_qtd)
        st.success("Quantidade atualizada com sucesso!")
        st.rerun()

    st.subheader("Atualizar preço de um produto")

    col3, col4 = st.columns(2)

    with col3:
        produto_preco = st.selectbox("Selecione o produto para atualizar preço", nomes_produtos, key="editar_preco_prod")
    with col4:
        novo_preco = st.number_input("Novo preço estimado", min_value=0.0, step=0.01, key="novo_preco")

    if st.button("Atualizar preço"):
        lista.atualizar_preco_produto(produto_preco, novo_preco)
        st.success("Preço atualizado com sucesso!")
        st.rerun()

    st.subheader("Excluir produto")

    produto_excluir = st.selectbox("Selecione o produto para excluir", nomes_produtos, key="excluir_prod")

    if st.button("Excluir produto"):
        lista.excluir_produto(produto_excluir)
        st.success("Produto excluído com sucesso!")
        st.rerun()