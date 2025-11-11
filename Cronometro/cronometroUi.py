# mi_cronometro.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QTimer, Qt
from cronometro import Cronometro

class CronometroWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Lógica
        self.crono = Cronometro()

        # Interfaz
        self.label = QLabel("00:00:00")
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_iniciar = QPushButton("Iniciar")
        self.btn_pausar = QPushButton("Pausar")
        self.btn_reiniciar = QPushButton("Reiniciar")  # NUEVO BOTÓN

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_iniciar)
        layout.addWidget(self.btn_pausar)
        layout.addWidget(self.btn_reiniciar)  # agregamos al layout
        self.setLayout(layout)

        # Temporizador
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar)

        # Botones
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_pausar.clicked.connect(self.pausar)
        self.btn_reiniciar.clicked.connect(self.reiniciar)  # conexión del nuevo botón

    def iniciar(self):
        self.crono.reiniciar()
        self.timer.start(1000)
        self.btn_pausar.setText("Pausar")

    def pausar(self):
        if self.timer.isActive():
            self.crono.pausar()
            self.timer.stop()
            self.btn_pausar.setText("Continuar")
        else:
            self.crono.continuar()
            self.timer.start(1000)
            self.btn_pausar.setText("Pausar")

    def reiniciar(self):
        # Reinicia el cronómetro sin arrancarlo
        self.crono.reiniciar()
        self.label.setText("00:00:00")
        self.timer.stop()
        self.btn_pausar.setText("Pausar")

    def actualizar(self):
        tiempo = self.crono.getTime().toString("hh:mm:ss")
        self.label.setText(tiempo)
