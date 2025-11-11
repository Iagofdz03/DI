# cronometro.py
from PySide6.QtCore import QElapsedTimer, QTime

class Cronometro:
    def __init__(self):
        self._tiempo_transcurrido = QElapsedTimer()
        self._tiempo_pausa = QElapsedTimer()
        self.acumulador = 0

    def reiniciar(self):
        self._tiempo_transcurrido.restart()
        self.acumulador = 0

    def getTime(self):
        return QTime(0, 0).addMSecs(self._tiempo_transcurrido.elapsed() - self.acumulador)

    def pausar(self):
        self._tiempo_pausa.restart()

    def continuar(self):
        self.acumulador += self._tiempo_pausa.elapsed()
