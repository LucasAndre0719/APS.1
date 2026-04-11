from datetime import time, datetime


class Horario:
    def __init__(self, hora: time):
        self.hora = hora
        self.tomado = False
        self.atrasado = False

    def verificar_atraso(self):
        agora = datetime.now().time()
        if not self.tomado and agora > self.hora:
            self.atrasado = True

    def remarcar(self, nova_hora: time):
        self.hora = nova_hora
        self.atrasado = False

    def marcar_como_tomado(self):
        self.tomado = True
        self.atrasado = False