from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import resources_rc  # necesario para que Qt encuentre los iconos

class ProductoConIcono(QWidget):
    def __init__(self, icono, nombre, precio, parent=None):
        super().__init__(parent)

        # Icono
        self.label_icono = QLabel()
        pixmap = QPixmap(icono)
        self.label_icono.setPixmap(pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.label_icono.setAlignment(Qt.AlignCenter)

        # Nombre y precio
        self.label_nombre = QLabel(nombre)
        self.label_nombre.setAlignment(Qt.AlignCenter)
        self.label_precio = QLabel(precio)
        self.label_precio.setAlignment(Qt.AlignCenter)

        # Layout vertical para nombre y precio
        layout_texto = QVBoxLayout()
        layout_texto.addWidget(self.label_nombre)
        layout_texto.addWidget(self.label_precio)
        layout_texto.setAlignment(Qt.AlignCenter)

        # Layout principal horizontal (icono + texto)
        layout_principal = QHBoxLayout()
        layout_principal.addWidget(self.label_icono)
        layout_principal.addLayout(layout_texto)
        layout_principal.setAlignment(Qt.AlignCenter)

        self.setLayout(layout_principal)
