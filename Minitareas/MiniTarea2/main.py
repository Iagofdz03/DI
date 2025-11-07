# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from t2_moneylineedit import MoneyLineEdit

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Crear ventana principal y layout vertical
    w = QWidget()
    layout = QVBoxLayout(w)

    # Crear los widgets
    txt = MoneyLineEdit()
    lbl = QLabel("Valor:")

    # Conectar la señal personalizada al cambio de texto del label
    txt.valueChanged.connect(lambda v: lbl.setText(f"Valor: {v:.2f} €"))

    # Añadirlos al layout
    layout.addWidget(txt)
    layout.addWidget(lbl)

    # Mostrar ventana
    w.show()
    sys.exit(app.exec())
