# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QToolButton

class SearchInput(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # elimina márgenes para que quede más compacto

        self.text = QLineEdit(placeholderText="Buscar…")
        self.btn = QToolButton(text="✖")

        # botón que limpia el texto
        self.btn.clicked.connect(self.text.clear)

        layout.addWidget(self.text)
        layout.addWidget(self.btn)
