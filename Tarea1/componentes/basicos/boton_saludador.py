from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel

class BotonSaludador(QWidget):
    def __init__(self):
        super().__init__()
        self.lbl = QLabel("Esperando clic…")
        self.btn = QPushButton("Saludar")

        layout = QVBoxLayout(self)
        layout.addWidget(self.lbl)
        layout.addWidget(self.btn)

        self.btn.clicked.connect(self.on_saludar)

    @Slot()
    def on_saludar(self):
        self.lbl.setText("¡Hola! Señal recibida")
