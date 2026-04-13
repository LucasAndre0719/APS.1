import streamlit as st
from datetime import date
from models import Remedio

st.set_page_config(page_title="Controle de Remédios", layout="centered")
st.title("Aplicação - Controle de Remédios")

if "remedio" not in st.session_state:
    st.session_state.remedio = None

nome_paciente = st.text_input("Nome do paciente")
nome_remedio = st.text_input("Nome do remédio")
dosagem = st.text_input("Dosagem")
data_inicio = st.date_input("Data de início", value=date.today())
qtd_dias = st.number_input("Quantidade de dias", min_value=1, value=7)
vezes_ao_dia = st.number_input("Vezes ao dia", min_value=1, value=3)

if st.button("Cadastrar"):
    st.session_state.remedio = Remedio(
        nome_paciente, data_inicio, int(qtd_dias), int(vezes_ao_dia), dosagem, nome_remedio
    )
    st.success("Remédio cadastrado com sucesso.")

if st.button("Sugerir horários") and st.session_state.remedio is not None:
    st.session_state.remedio.sugerirHorario()

if st.session_state.remedio is not None:
    remedio = st.session_state.remedio
    st.write(remedio.cadastrar())
    st.write("Data final:", remedio.calcularDataFim())

    for i, horario in enumerate(remedio.horarios):
        st.write(f"Horário {i+1}: {horario.hora}")