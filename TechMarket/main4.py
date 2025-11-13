import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from producto_con_icono import ProductoConIcono

class VentanaProductos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini 4 – Productos con icono")

        # Layout principal vertical
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        # Crear productos usando rutas de recurso
        p1 = ProductoConIcono("icons/laptop.png", "Portátil ZenAir", "799 €")
        p2 = ProductoConIcono("icons/mouse.png", "Ratón Ergonomic", "25 €")
        p3 = ProductoConIcono("icons/keyboard.png", "Teclado Gamer RGB", "99 €")

        # Añadirlos al layout
        layout.addWidget(p1)
        layout.addWidget(p2)
        layout.addWidget(p3)

        self.setLayout(layout)
        self.resize(300, 400)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaProductos()
    ventana.show()
    sys.exit(app.exec())
