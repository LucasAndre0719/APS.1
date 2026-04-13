import streamlit as st


# =========================
# CLASSES
# =========================

class Produto:
    def __init__(self, nome: str, valorUnitario: float):
        self.nome = nome
        self.valorUnitario = valorUnitario

    def exibirProduto(self):
        return f"{self.nome} - R$ {self.valorUnitario:.2f}"


class ItemComanda:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade
        self.subtotal = self.calcularSubtotal()

    def calcularSubtotal(self):
        return self.produto.valorUnitario * self.quantidade


class Comanda:
    def __init__(self, numero: int):
        self.numero = numero
        self.itens = []
        self.total = 0.0

    def registrarProduto(self, produto: Produto, quantidade: int):
        item = ItemComanda(produto, quantidade)
        self.itens.append(item)
        self.calcularTotal()

    def calcularTotal(self):
        self.total = sum(item.subtotal for item in self.itens)
        return self.total

    def exibirComanda(self):
        return [
            {
                "Produto": item.produto.nome,
                "Quantidade": item.quantidade,
                "Valor Unitário": item.produto.valorUnitario,
                "Subtotal": item.subtotal
            }
            for item in self.itens
        ]

    def finalizarCompra(self):
        self.itens = []
        self.total = 0.0


# =========================
# STREAMLIT
# =========================

st.set_page_config(page_title="Comanda", layout="centered")
st.title("Sistema de Comanda")

# Criar comanda na sessão
if "comanda" not in st.session_state:
    st.session_state.comanda = Comanda(numero=1)

# Lista de produtos fixos (pode melhorar depois)
produtos_disponiveis = [
    Produto("Hambúrguer", 20.0),
    Produto("Pizza", 35.0),
    Produto("Refrigerante", 8.0),
    Produto("Batata Frita", 15.0)
]

st.subheader("Adicionar produto")

produto_nome = st.selectbox(
    "Escolha o produto",
    [p.nome for p in produtos_disponiveis]
)

quantidade = st.number_input("Quantidade", min_value=1, value=1)

# Encontrar produto selecionado
produto_selecionado = next(p for p in produtos_disponiveis if p.nome == produto_nome)

if st.button("Adicionar à comanda"):
    st.session_state.comanda.registrarProduto(produto_selecionado, quantidade)
    st.success("Produto adicionado!")

# =========================
# EXIBIR COMANDA
# =========================

st.markdown("---")
st.subheader("Comanda atual")

dados = st.session_state.comanda.exibirComanda()

if dados:
    st.dataframe(dados, use_container_width=True)
    total = st.session_state.comanda.calcularTotal()
    st.write(f"### Total: R$ {total:.2f}")
else:
    st.info("Nenhum item na comanda.")

# =========================
# FINALIZAR
# =========================

if st.button("Finalizar compra"):
    total_final = st.session_state.comanda.total
    st.success(f"Compra finalizada! Total: R$ {total_final:.2f}")
    st.session_state.comanda.finalizarCompra()