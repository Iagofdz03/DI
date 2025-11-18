from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from micomponente import MiComponente

class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formulario sin Qt Designer")

        layout = QVBoxLayout()

        # Aquí añadimos directamente tu componente promocionado
        self.mi_componente = MiComponente()
        layout.addWidget(self.mi_componente)

        self.setLayout(layout)


app = QApplication([])
window = Ventana()
window.show()
app.exec()
