# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Signal

class MoneyLineEdit(QLineEdit):
    valueChanged = Signal(float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.textChanged.connect(self.on_text_changed)

    def on_text_changed(self, txt):
        try:
            val = float(txt.replace(",", "."))
            self.valueChanged.emit(val)
        except:
            pass
