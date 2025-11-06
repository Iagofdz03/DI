# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from interfaz import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Aquí puedes conectar señales o añadir lógica
        self.ui.pushButton_2.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("¡Has hecho clic en el botón!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
