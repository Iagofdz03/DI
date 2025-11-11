# main.py
import sys
from PySide6.QtWidgets import QApplication
from cronometroUi import CronometroWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = CronometroWidget()
    ventana.setWindowTitle("Mini Cronómetro")
    ventana.resize(200, 150)
    ventana.show()

    sys.exit(app.exec())
