# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QBrush, QPen
from PySide6.QtCore import Qt

class BatteryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._level = 50  # nivel inicial
        self.setMinimumSize(150, 50)

    def setLevel(self, val):
        # Limita el valor entre 0 y 100
        self._level = max(0, min(100, val))
        self.update()  # fuerza el repintado

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        # Dibuja el contorno de la batería
        p.setPen(QPen(Qt.black, 2))
        p.drawRect(10, 10, 120, 30)

        # Color según el nivel
        color = QColor("red") if self._level < 20 else QColor("green")
        p.setBrush(QBrush(color))

        # Dibuja el nivel de carga
        p.drawRect(12, 12, int(1.16 * self._level), 26)

        # Dibuja el terminal de la batería
        p.setBrush(QBrush(Qt.black))
        p.drawRect(132, 18, 6, 14)
