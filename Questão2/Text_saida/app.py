import streamlit as st
from models import TextoSaida, COR, TipoComponente

st.set_page_config(page_title="Texto Saída", layout="centered")

st.title("Aplicação - TextoSaida")

texto = st.text_area("Digite o texto", "Olá, esse é um exemplo de texto.")
tamanho_fonte = st.slider("Tamanho da Fonte", 10, 50, 20)

cor_fonte = st.selectbox("Cor da Fonte", [cor.name for cor in COR])
cor_fundo = st.selectbox("Cor de Fundo", [cor.name for cor in COR])
tipo_componente = st.selectbox("Tipo de Componente", [tipo.name for tipo in TipoComponente])

if st.button("Exibir"):
    componente = TextoSaida(
        tamanhoFonte=tamanho_fonte,
        cor_fonte=COR[cor_fonte],
        cor_fundo=COR[cor_fundo],
        texto=texto,
        tipoComponente=TipoComponente[tipo_componente]
    )

    estilo = f"""
    <div style="
        font-size: {componente.tamanhoFonte}px;
        color: {componente.cor_fonte.value};
        background-color: {componente.cor_fundo.value};
        padding: 10px;
        border-radius: 8px;
        margin-top: 10px;
        white-space: pre-wrap;
    ">
        {componente.texto}
    </div>
    """

    if componente.tipoComponente == TipoComponente.label:
        st.markdown(estilo, unsafe_allow_html=True)

    elif componente.tipoComponente == TipoComponente.edit:
        st.text_input("Campo Editável", value=componente.texto)

    elif componente.tipoComponente == TipoComponente.memo:
        st.text_area("Área de texto", value=componente.texto, height=150)