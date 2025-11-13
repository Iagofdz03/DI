# main.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from buscador import Ui_MainWindow  # tu archivo .py generado del .ui

class Buscador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Lista de todos los labels y sus textos
        self.labels = [
            self.ui.label,
            self.ui.label_4,
            self.ui.label_5,
            self.ui.label_2,
            self.ui.label_3
        ]

        # Guardamos los nombres de los productos
        self.productos = [label.text() for label in self.labels]

        # Conectamos el QLineEdit al método de filtrado
        self.ui.lineEdit.textChanged.connect(self.filtrar)

        # Cambiamos el título de la ventana
        self.setWindowTitle("Mini 1 – Buscador de productos")

    def filtrar(self, texto):
        texto = texto.lower()
        for label, producto in zip(self.labels, self.productos):
            if texto in producto.lower() or texto == "":
                label.show()
            else:
                label.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Buscador()
    ventana.show()
    sys.exit(app.exec())
