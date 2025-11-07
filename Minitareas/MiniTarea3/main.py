# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider
from PySide6.QtCore import Qt
from t3_batterywidget import BatteryWidget

app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle("Mini-tarea 3 - Battery Widget")

layout = QVBoxLayout(w)
battery = BatteryWidget()
slider = QSlider(Qt.Horizontal)

slider.setRange(0, 100)
slider.setValue(50)
slider.valueChanged.connect(battery.setLevel)

layout.addWidget(battery)
layout.addWidget(slider)

w.show()
sys.exit(app.exec())
