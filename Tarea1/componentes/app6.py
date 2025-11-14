from PySide6.QtWidgets import QApplication, QMainWindow
from componentes.panel_empleados import PanelEmpleados

app = QApplication([])
win = QMainWindow()
win.setCentralWidget(PanelEmpleados())
win.show()
app.exec()
