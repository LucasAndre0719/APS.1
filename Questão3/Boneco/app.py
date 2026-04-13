import streamlit as st
from models import BonecoEmMovimento

st.set_page_config(page_title="Boneco em Movimento", layout="centered")
st.title("Aplicação - Boneco em Movimento")

if "boneco" not in st.session_state:
    st.session_state.boneco = BonecoEmMovimento("Boneco")

nome = st.text_input("Nome do boneco", st.session_state.boneco.nome)
st.session_state.boneco.nome = nome

st.write(f"**Nome:** {st.session_state.boneco.nome}")
st.write(f"**X:** {st.session_state.boneco.coord_x}")
st.write(f"**Y:** {st.session_state.boneco.coord_y}")
st.write(f"**Direção:** {st.session_state.boneco.direcao_atual.value}")

col1, col2, col3 = st.columns(3)

with col2:
    if st.button("⬆ Cima"):
        st.session_state.boneco.mover_cima()

with col1:
    if st.button("⬅ Esquerda"):
        st.session_state.boneco.mover_esquerda()

with col3:
    if st.button("➡ Direita"):
        st.session_state.boneco.mover_direita()

with col2:
    if st.button("⬇ Baixo"):
        st.session_state.boneco.mover_baixo()