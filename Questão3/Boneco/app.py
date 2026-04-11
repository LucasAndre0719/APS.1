import streamlit as st
import matplotlib.pyplot as plt
from boneco import BonecoEmMovimento

st.set_page_config(page_title="Boneco em Movimento", page_icon="🕹️")
st.title("Aplicação - Boneco em Movimento")

if "boneco" not in st.session_state:
    st.session_state.boneco = None

st.subheader("Criar boneco")

with st.form("form_boneco"):
    nome = st.text_input("Nome do boneco", value="Boneco 1")
    coord_x = st.number_input("Coordenada X inicial", value=0.0, step=1.0)
    coord_y = st.number_input("Coordenada Y inicial", value=0.0, step=1.0)
    criar = st.form_submit_button("Criar boneco")

if criar:
    st.session_state.boneco = BonecoEmMovimento(nome, coord_x, coord_y)
    st.success("Boneco criado com sucesso!")

if st.session_state.boneco is not None:
    boneco = st.session_state.boneco

    st.subheader("Dados do boneco")
    st.write(f"**Nome:** {boneco.nome}")
    st.write(f"**Posição X:** {boneco.coord_x}")
    st.write(f"**Posição Y:** {boneco.coord_y}")
    st.write(f"**Direção atual:** {boneco.direcao_atual.value}")

    st.subheader("Mover boneco")

    col1, col2, col3 = st.columns(3)

    with col2:
        if st.button("⬆️ Cima"):
            boneco.mover_cima()

    with col1:
        if st.button("⬅️ Esquerda"):
            boneco.mover_esquerda()

    with col2:
        if st.button("⬇️ Baixo"):
            boneco.mover_baixo()

    with col3:
        if st.button("➡️ Direita"):
            boneco.mover_direita()

    st.subheader("Visualização")

    fig, ax = plt.subplots()
    ax.scatter(boneco.coord_x, boneco.coord_y, s=300, marker="o")
    ax.text(boneco.coord_x, boneco.coord_y + 0.3, boneco.nome, ha="center")

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Posição do Boneco")
    ax.grid(True)

    st.pyplot(fig)