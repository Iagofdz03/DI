from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QMessageBox
from PySide6.QtCore import Slot

from componentes.basicos.boton_saludador import BotonSaludador
from componentes.empresa.panel_empleados import PanelEmpleados

app = QApplication([])
win = QMainWindow()

cont = QWidget()
lay = QVBoxLayout(cont)

a = BotonSaludador()
b = PanelEmpleados()

lay.addWidget(a)
lay.addWidget(b)

@Slot(str)
def avisar(mensaje):
    QMessageBox.information(win, "Evento", mensaje)

a.saludado.connect(avisar)

win.setCentralWidget(cont)
win.show()
app.exec()
