# main.py
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QLineEdit, QPushButton, QScrollArea, QMainWindow
)
from PySide6.QtCore import Qt


# -------------------------------
# Componente Producto (reutilizado)
# -------------------------------
class Producto(QWidget):
    def __init__(self, nombre: str, precio: str, parent=None):
        super().__init__(parent)
        self._nombre = nombre
        self._precio = precio

        # Etiquetas
        self.label_nombre = QLabel(self._nombre)
        self.label_precio = QLabel(self._precio)

        # Estilo
        self.label_nombre.setStyleSheet("font-weight: bold; font-size: 14px;")
        self.label_precio.setStyleSheet("color: gray;")

        layout = QVBoxLayout()
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.label_precio)
        self.setLayout(layout)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        self.label_nombre.setText(valor)

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = valor
        self.label_precio.setText(valor)


# -------------------------------
# Contenedor de productos con filtro
# -------------------------------
class ListaProductos(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Lista de objetos Producto
        self.productos = [
            Producto("Portátil ZenAir", "799 €"),
            Producto("Ratón Ergonomic", "25 €"),
            Producto("Teclado Gamer RGB", "99 €"),
            Producto("Monitor Curvo 27''", "249 €"),
            Producto("Webcam 4K", "120 €")
        ]

        # Campo de búsqueda
        self.buscador = QLineEdit()
        self.buscador.setPlaceholderText("Buscar productos...")
        self.buscador.textChanged.connect(self.filtrar)

        # Contenedor de productos
        self.contenedor = QWidget()
        self.layout_productos = QVBoxLayout(self.contenedor)
        self.layout_productos.setAlignment(Qt.AlignTop)

        for p in self.productos:
            self.layout_productos.addWidget(p)

        # Scroll area
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.contenedor)

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.buscador)
        layout.addWidget(self.scroll)
        self.setLayout(layout)

    def filtrar(self, texto):
        texto = texto.lower().strip()
        for p in self.productos:
            # Mostrar si el nombre contiene el texto
            visible = texto in p.nombre.lower() or texto == ""
            p.setVisible(visible)


# -------------------------------
# Ventana principal
# -------------------------------
class CatalogoVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini 3 – Catálogo con buscador")
        self.resize(400, 400)

        self.lista = ListaProductos()
        self.setCentralWidget(self.lista)


# -------------------------------
# Ejecución
# -------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CatalogoVentana()
    ventana.show()
    sys.exit(app.exec())
