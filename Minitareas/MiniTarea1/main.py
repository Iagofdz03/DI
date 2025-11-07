# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Cargar el archivo de la interfaz
    loader = QUiLoader()
    ui_file = QFile("ui/t1_switch.ui")  # asegúrate de que está en la misma carpeta
    ui_file.open(QFile.ReadOnly)
    w = loader.load(ui_file)
    ui_file.close()

    # Personalizar el aspecto (QCheckBox → Switch)
    w.chckSwitch.setStyleSheet("""
    QCheckBox::indicator { width: 46px; height: 24px; }
    QCheckBox::indicator:unchecked { border-radius: 12px; background:#ccc; }
    QCheckBox::indicator:checked { border-radius: 12px; background:#2ecc71; }
    """)

    # Cambiar el texto según el estado
    w.chckSwitch.toggled.connect(lambda s: w.chckSwitch.setText("ON" if s else "OFF"))

    # Mostrar ventana
    w.show()
    sys.exit(app.exec())
