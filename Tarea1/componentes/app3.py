from PySide6.QtWidgets import QApplication, QMainWindow
from componentes.etiqueta_saludo import EtiquetaSaludo

app = QApplication([])
win = QMainWindow()
win.setWindowTitle("Reutilizando un componente")
win.setCentralWidget(EtiquetaSaludo("Hola desde mi componente"))
win.show()
app.exec()
