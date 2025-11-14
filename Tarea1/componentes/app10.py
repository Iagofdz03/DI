from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QMessageBox
)
from PySide6.QtCore import Slot

from componentes.basicos.boton_saludador import BotonSaludador
from componentes.empresa.panel_empleados import PanelEmpleados


app = QApplication([])

win = QMainWindow()
win.setWindowTitle("Mini-tarea 10 — Reutilización de Componentes")

tabs = QTabWidget()

# Crear los componentes
widget_saludo = BotonSaludador()
widget_empleados = PanelEmpleados()

# Añadir pestañas
tabs.addTab(widget_saludo, "Saludo")
tabs.addTab(widget_empleados, "Empleados")

# Slot para mostrar mensaje cuando se emite la señal
@Slot(str)
def avisar(mensaje):
    QMessageBox.information(win, "Evento", mensaje)

# Conectar señal del BotonSaludador
widget_saludo.saludado.connect(avisar)

win.setCentralWidget(tabs)
win.resize(500, 400)
win.show()

app.exec()
