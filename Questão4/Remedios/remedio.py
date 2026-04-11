from datetime import datetime, timedelta, time
from horario import Horario


class Remedio:
    def __init__(self, nome_paciente, nome_remedio, data_inicio, qtd_dias, vezes_ao_dia, dosagem):
        self.nome_paciente = nome_paciente
        self.nome_remedio = nome_remedio
        self.data_inicio = data_inicio
        self.qtd_dias = qtd_dias
        self.vezes_ao_dia = vezes_ao_dia
        self.dosagem = dosagem
        self.horarios = []

    def sugerir_horarios(self):
        self.horarios = []

        intervalo = 24 // self.vezes_ao_dia
        hora_base = 8  # começa às 08:00

        for i in range(self.vezes_ao_dia):
            h = (hora_base + i * intervalo) % 24
            self.horarios.append(Horario(time(hour=h)))

    def calcular_data_fim(self):
        return self.data_inicio + timedelta(days=self.qtd_dias)

    def reorganizar_horarios(self):
        for h in self.horarios:
            if h.atrasado:
                nova_hora = (datetime.combine(datetime.today(), h.hora) + timedelta(hours=1)).time()
                h.remarcar(nova_hora)