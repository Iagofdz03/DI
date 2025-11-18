from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class MiComponente(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()
        self.label = QLabel("Hola! Soy un componente personalizado")
        layout.addWidget(self.label)
        self.setLayout(layout)
