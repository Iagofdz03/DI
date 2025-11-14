from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class EtiquetaSaludo(QWidget):
    def __init__(self, texto="Hola 👋"):
        super().__init__()
        self.lbl = QLabel(texto)
        layout = QVBoxLayout(self)
        layout.addWidget(self.lbl)
