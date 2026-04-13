from datetime import date, time, timedelta
import pandas as pd


class Horario:
    def __init__(self, hora: time, tomado: bool = False, atrasado: bool = False):
        self.hora = hora
        self.tomado = tomado
        self.atrasado = atrasado

    def remarcar(self, nova_hora: time):
        self.hora = nova_hora
        self.atrasado = False

    def exibir(self):
        return {
            "Hora": self.hora.strftime("%H:%M"),
            "Tomado": "Sim" if self.tomado else "Não",
            "Atrasado": "Sim" if self.atrasado else "Não"
        }


class Remedio:
    def __init__(self, nomePaciente, dataInicio, qtdDias, vezesAoDia, dosagem, nomeRemedio):
        self.nomePaciente = nomePaciente
        self.dataInicio = dataInicio
        self.qtdDias = qtdDias
        self.vezesAoDia = vezesAoDia
        self.dosagem = dosagem
        self.nomeRemedio = nomeRemedio
        self.horarios = []

    def cadastrar(self):
        return f"Remédio {self.nomeRemedio} cadastrado com sucesso para {self.nomePaciente}."

    def sugerirHorario(self):
        self.horarios = []
        intervalo = 24 / self.vezesAoDia
        hora_base = 6

        for i in range(self.vezesAoDia):
            hora_calculada = int((hora_base + i * intervalo) % 24)
            minuto_calculado = int((((hora_base + i * intervalo) % 1) * 60))
            self.horarios.append(Horario(time(hora_calculada, minuto_calculado)))

    def calcularDataFim(self):
        return self.dataInicio + timedelta(days=self.qtdDias - 1)

    def gerarPlanilha(self):
        dados = []
        data_fim = self.calcularDataFim()
        data_atual = self.dataInicio

        while data_atual <= data_fim:
            for horario in self.horarios:
                dados.append({
                    "Paciente": self.nomePaciente,
                    "Remédio": self.nomeRemedio,
                    "Dosagem": self.dosagem,
                    "Data": data_atual.strftime("%d/%m/%Y"),
                    "Hora": horario.hora.strftime("%H:%M"),
                    "Tomado": "Sim" if horario.tomado else "Não",
                    "Atrasado": "Sim" if horario.atrasado else "Não"
                })
            data_atual += timedelta(days=1)

        return pd.DataFrame(dados)

    def reorganizarHorarios(self, nova_primeira_hora):
        self.horarios = []
        intervalo = 24 / self.vezesAoDia
        base_decimal = nova_primeira_hora.hour + nova_primeira_hora.minute / 60

        for i in range(self.vezesAoDia):
            horario_decimal = (base_decimal + i * intervalo) % 24
            hora_calculada = int(horario_decimal)
            minuto_calculado = int((horario_decimal - hora_calculada) * 60)
            self.horarios.append(Horario(time(hora_calculada, minuto_calculado)))