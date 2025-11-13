import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QLineEdit, QScrollArea, QPushButton, QMessageBox, QToolBar, QStatusBar
)
from PySide6.QtCore import Qt
from producto_con_icono import ProductoConIcono
import resources_rc  # necesario para cargar los iconos

class TechMarketDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TechMarket Dashboard")
        self.resize(400, 500)

        # ------------------------
        # Barra de herramientas
        # ------------------------
        toolbar = QToolBar("Mi Toolbar")
        self.addToolBar(toolbar)

        btn_add = QPushButton("Añadir producto")
        btn_remove = QPushButton("Eliminar producto")
        btn_stats = QPushButton("Mostrar estadísticas")
        toolbar.addWidget(btn_add)
        toolbar.addWidget(btn_remove)
        toolbar.addWidget(btn_stats)

        # Conectar botones
        btn_stats.clicked.connect(self.mostrar_estadisticas)
        btn_add.clicked.connect(self.añadir_producto)
        btn_remove.clicked.connect(self.eliminar_producto)

        # ------------------------
        # Buscador
        # ------------------------
        self.busqueda = QLineEdit()
        self.busqueda.setPlaceholderText("Buscar producto...")
        self.busqueda.textChanged.connect(self.filtrar_productos)

        # ------------------------
        # Lista de productos con scroll
        # ------------------------
        self.lista_widget = QWidget()
        self.lista_layout = QVBoxLayout()
        self.lista_layout.setAlignment(Qt.AlignTop)
        self.lista_widget.setLayout(self.lista_layout)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.lista_widget)

        # ------------------------
        # Layout central
        # ------------------------
        central = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.busqueda)
        layout.addWidget(self.scroll)
        central.setLayout(layout)
        self.setCentralWidget(central)

        # ------------------------
        # Barra de estado
        # ------------------------
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Listo")

        # ------------------------
        # Productos de ejemplo
        # ------------------------
        self.productos = []
        self.crear_productos_ejemplo()

    def crear_productos_ejemplo(self):
        ejemplos = [
            (":/icons/laptop.png", "Portátil ZenAir", "799 €"),
            (":/icons/mouse.png", "Ratón Ergonomic", "25 €"),
            (":/icons/keyboard.png", "Teclado Gamer RGB", "99 €")
        ]
        for icono, nombre, precio in ejemplos:
            p = ProductoConIcono(icono, nombre, precio)
            self.productos.append(p)
            self.lista_layout.addWidget(p)

    # ------------------------
    # Funcionalidad buscador
    # ------------------------
    def filtrar_productos(self, texto):
        texto = texto.lower()
        for p in self.productos:
            nombre = p.label_nombre.text().lower()
            p.setVisible(texto in nombre or texto == "")

    # ------------------------
    # Estadísticas
    # ------------------------
    def mostrar_estadisticas(self):
        total = len(self.productos)
        visibles = sum(1 for p in self.productos if p.isVisible())
        QMessageBox.information(self, "Estadísticas",
                                f"Total productos: {total}\nVisibles: {visibles}")

    # ------------------------
    # Añadir / eliminar producto
    # ------------------------
    def añadir_producto(self):
        # Ejemplo simple, siempre el mismo producto
        p = ProductoConIcono(":/icons/mouse.png", "Nuevo Ratón", "19 €")
        self.productos.append(p)
        self.lista_layout.addWidget(p)

    def eliminar_producto(self):
        # Elimina el último producto visible
        for p in reversed(self.productos):
            if p.isVisible():
                self.lista_layout.removeWidget(p)
                p.deleteLater()
                self.productos.remove(p)
                break

# ------------------------
# Ejecutar app
# ------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TechMarketDashboard()
    ventana.show()
    sys.exit(app.exec())
