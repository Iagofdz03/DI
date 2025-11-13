# main.py
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMainWindow

class Producto(QWidget):
    def __init__(self, nombre: str, precio: str, parent=None):
        super().__init__(parent)

        # Atributos privados
        self._nombre = nombre
        self._precio = precio

        # Labels
        self.label_nombre = QLabel(self._nombre)
        self.label_precio = QLabel(self._precio)

        # Layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.label_precio)
        self.setLayout(layout)

    # Propiedad nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        self.label_nombre.setText(valor)  # actualiza la etiqueta

    # Propiedad precio
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = valor
        self.label_precio.setText(valor)  # actualiza la etiqueta

# Ventana demo
class DemoProducto(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mini 2 – Componente Producto")

        # Widget central
        central = QWidget()
        self.setCentralWidget(central)

        # Creamos un producto
        self.producto = Producto("Ratón Óptico Pro", "19,99 €")

        # Botón para actualizar precio
        self.btn_actualizar = QPushButton("Actualizar precio")
        self.btn_actualizar.clicked.connect(self.actualizar_precio)

        # Layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.producto)
        layout.addWidget(self.btn_actualizar)
        central.setLayout(layout)

    def actualizar_precio(self):
        # Cambiamos el precio usando el setter
        self.producto.precio = "14,99 €"

# Ejecución
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = DemoProducto()
    ventana.show()
    sys.exit(app.exec())
