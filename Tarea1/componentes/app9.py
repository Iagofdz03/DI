import recursos_rc
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication([])
win = QMainWindow()

win.setWindowTitle("App con icono")
win.setWindowIcon(QIcon("icons/icono.png"))

win.show()
app.exec()
