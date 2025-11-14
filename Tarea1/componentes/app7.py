from PySide6.QtWidgets import QApplication, QMainWindow
from componentes.basicos.boton_saludador import BotonSaludador
from componentes.empresa.panel_empleados import PanelEmpleados

app = QApplication([])
win = QMainWindow()

win.setWindowTitle("Subpaquetes funcionando")

win.setCentralWidget(BotonSaludador())
win.show()
app.exec()
