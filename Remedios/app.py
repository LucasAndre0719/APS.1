import streamlit as st
from datetime import date
from remedio import Remedio

st.set_page_config(page_title="Controle de Remédios", page_icon="💊")
st.title("Controle de Horários de Remédios")

# estado
if "remedio" not in st.session_state:
    st.session_state.remedio = None

# formulário
st.subheader("Cadastrar Remédio")

with st.form("form_remedio"):
    nome_paciente = st.text_input("Nome do paciente")
    nome_remedio = st.text_input("Nome do remédio")
    data_inicio = st.date_input("Data de início", value=date.today())
    qtd_dias = st.number_input("Quantidade de dias", min_value=1)
    vezes_ao_dia = st.number_input("Vezes ao dia", min_value=1, max_value=6)
    dosagem = st.text_input("Dosagem")

    cadastrar = st.form_submit_button("Cadastrar")

if cadastrar:
    r = Remedio(nome_paciente, nome_remedio, data_inicio, qtd_dias, vezes_ao_dia, dosagem)
    r.sugerir_horarios()
    st.session_state.remedio = r
    st.success("Remédio cadastrado e horários sugeridos!")

# exibição
if st.session_state.remedio:
    r = st.session_state.remedio

    st.subheader("Dados do Remédio")
    st.write(f"Paciente: {r.nome_paciente}")
    st.write(f"Remédio: {r.nome_remedio}")
    st.write(f"Dosagem: {r.dosagem}")
    st.write(f"Data fim: {r.calcular_data_fim()}")

    st.subheader("Horários do dia")

    for i, h in enumerate(r.horarios):
        h.verificar_atraso()

        col1, col2, col3 = st.columns([2, 1, 1])

        with col1:
            status = "⏰ Atrasado" if h.atrasado else ("✅ Tomado" if h.tomado else "⏳ Pendente")
            st.write(f"{h.hora.strftime('%H:%M')} - {status}")

        with col2:
            if st.button(f"Tomado {i}"):
                h.marcar_como_tomado()

        with col3:
            if st.button(f"Remarcar {i}"):
                r.reorganizar_horarios()
