# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from t4_searchinput import SearchInput

app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle("Mini-tarea 4 - SearchInput")

layout = QVBoxLayout(w)
search = SearchInput()
lbl = QLabel("0 caracteres")

# actualiza el contador en tiempo real
search.text.textChanged.connect(lambda t: lbl.setText(f"{len(t)} caracteres"))

layout.addWidget(search)
layout.addWidget(lbl)

w.show()
sys.exit(app.exec())
