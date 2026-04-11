import streamlit as st
from texto_saida import TextoSaida, Cor, TipoComponente

st.set_page_config(page_title="Classe TextoSaida", page_icon="📝")
st.title("Aplicação - Classe TextoSaida")

st.write("Configure o texto e escolha como ele será exibido.")

texto = st.text_area("Texto", value="Olá, mundo!")

tamanho_fonte = st.slider("Tamanho da fonte", min_value=10, max_value=50, value=20)

cor_fonte_str = st.selectbox(
    "Cor da fonte",
    [cor.value for cor in Cor]
)

cor_fundo_str = st.selectbox(
    "Cor do fundo",
    [cor.value for cor in Cor],
    index=1
)

tipo_componente_str = st.selectbox(
    "Tipo de componente",
    [tipo.value for tipo in TipoComponente]
)

if st.button("Exibir texto"):
    cor_fonte = Cor(cor_fonte_str)
    cor_fundo = Cor(cor_fundo_str)
    tipo_componente = TipoComponente(tipo_componente_str)

    texto_saida = TextoSaida(
        texto=texto,
        tamanho_fonte=tamanho_fonte,
        cor_fonte=cor_fonte,
        cor_fundo=cor_fundo,
        tipo_componente=tipo_componente
    )

    st.subheader("Resultado")
    st.markdown(texto_saida.exibir(), unsafe_allow_html=True)