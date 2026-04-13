import streamlit as st
import pandas as pd


# =========================
# CLASSE PRODUTO
# =========================
class ProdutoCompra:
    def __init__(self, nome, unidadeCompra, qtdMes, qtdCompra, precoEstimado):
        self.nome = nome
        self.unidadeCompra = unidadeCompra
        self.qtdMes = qtdMes
        self.qtdCompra = qtdCompra
        self.precoEstimado = precoEstimado
        self.subtotal = self.calcularSubtotal()

    def calcularSubtotal(self):
        return self.qtdCompra * self.precoEstimado

    def atualizarPreco(self, novoPreco):
        self.precoEstimado = novoPreco
        self.subtotal = self.calcularSubtotal()

    def exibir(self):
        return {
            "Produto": self.nome,
            "Unidade": self.unidadeCompra,
            "Qtd Mês": self.qtdMes,
            "Qtd Compra": self.qtdCompra,
            "Preço": self.precoEstimado,
            "Subtotal": self.subtotal
        }


# =========================
# CLASSE LISTA
# =========================
class ListaCompra:
    def __init__(self):
        self.itens = []
        self.total = 0.0

    def adicionarProduto(self, produto):
        self.itens.append(produto)
        self.calcularTotal()

    def calcularTotal(self):
        self.total = sum(p.subtotal for p in self.itens)
        return self.total

    def listarProdutos(self):
        return [p.exibir() for p in self.itens]

    def atualizarPrecoProduto(self, index, novoPreco):
        if 0 <= index < len(self.itens):
            self.itens[index].atualizarPreco(novoPreco)
            self.calcularTotal()


# =========================
# STREAMLIT
# =========================

st.set_page_config(page_title="Lista de Compras", layout="centered")
st.title("Sistema de Lista de Compras")

if "lista" not in st.session_state:
    st.session_state.lista = ListaCompra()

# =========================
# CADASTRO
# =========================
st.subheader("Adicionar produto")

nome = st.text_input("Nome do produto")
unidade = st.selectbox("Unidade de compra", ["kg", "litro", "unidade", "caixa"])
qtd_mes = st.number_input("Quantidade mensal", min_value=0.0, value=1.0)
qtd_compra = st.number_input("Quantidade a comprar", min_value=0.0, value=1.0)
preco = st.number_input("Preço estimado", min_value=0.0, value=1.0)

if st.button("Adicionar produto"):
    produto = ProdutoCompra(nome, unidade, qtd_mes, qtd_compra, preco)
    st.session_state.lista.adicionarProduto(produto)
    st.success("Produto adicionado!")

# =========================
# LISTA
# =========================
st.markdown("---")
st.subheader("Lista de produtos")

dados = st.session_state.lista.listarProdutos()

if dados:
    df = pd.DataFrame(dados)
    st.dataframe(df, use_container_width=True)

    total = st.session_state.lista.calcularTotal()
    st.write(f"### Total da compra: R$ {total:.2f}")
else:
    st.info("Nenhum produto na lista.")

# =========================
# ATUALIZAR PREÇO
# =========================
st.markdown("---")
st.subheader("Atualizar preço")

if st.session_state.lista.itens:
    nomes = [p.nome for p in st.session_state.lista.itens]

    indice = st.selectbox("Escolha o produto", range(len(nomes)), format_func=lambda i: nomes[i])
    novo_preco = st.number_input("Novo preço", min_value=0.0, value=1.0)

    if st.button("Atualizar preço"):
        st.session_state.lista.atualizarPrecoProduto(indice, novo_preco)
        st.success("Preço atualizado!")
        st.rerun()