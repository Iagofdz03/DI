# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget,
    QVBoxLayout, QLabel, QSlider, QCheckBox, QStatusBar
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

# ===== Importa tus widgets personalizados =====
from t2_moneylineedit import MoneyLineEdit
from t3_batterywidget import BatteryWidget
from t4_searchinput import SearchInput


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CustomWidgetsCompany")
        self.setWindowIcon(QIcon("icons/logo.png"))

        # Crea las pestañas
        tabs = QTabWidget()
        tabs.addTab(self.make_task1_tab(), "Switch")
        tabs.addTab(self.make_task2_tab(), "MoneyLineEdit")
        tabs.addTab(self.make_task3_tab(), "Battery")
        tabs.addTab(self.make_task4_tab(), "SearchInput")

        self.setCentralWidget(tabs)

        # Status bar
        status = QStatusBar()
        status.showMessage("Listo")
        self.setStatusBar(status)

    # ---------- Mini-tarea 1 ----------
    def make_task1_tab(self):
        w = QWidget()
        layout = QVBoxLayout(w)

        chk = QCheckBox("OFF")
        chk.setStyleSheet("""
        QCheckBox::indicator { width: 46px; height: 24px; }
        QCheckBox::indicator:unchecked { border-radius: 12px; background:#ccc; }
        QCheckBox::indicator:checked { border-radius: 12px; background:#2ecc71; }
        """)
        chk.toggled.connect(lambda s: chk.setText("ON" if s else "OFF"))

        layout.addWidget(QLabel("Interruptor estilo switch:"))
        layout.addWidget(chk)
        layout.addStretch()
        return w

    # ---------- Mini-tarea 2 ----------
    def make_task2_tab(self):
        w = QWidget()
        layout = QVBoxLayout(w)

        txt = MoneyLineEdit()
        lbl = QLabel("Valor: 0.00 €")
        txt.valueChanged.connect(lambda v: lbl.setText(f"Valor: {v:.2f} €"))

        layout.addWidget(QLabel("Introduce un valor monetario:"))
        layout.addWidget(txt)
        layout.addWidget(lbl)
        layout.addStretch()
        return w

    # ---------- Mini-tarea 3 ----------
    def make_task3_tab(self):
        w = QWidget()
        layout = QVBoxLayout(w)

        battery = BatteryWidget()
        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 100)
        slider.setValue(50)
        slider.valueChanged.connect(battery.setLevel)

        layout.addWidget(QLabel("Nivel de batería:"))
        layout.addWidget(battery)
        layout.addWidget(slider)
        layout.addStretch()
        return w

    # ---------- Mini-tarea 4 ----------
    def make_task4_tab(self):
        w = QWidget()
        layout = QVBoxLayout(w)

        s = SearchInput()
        lbl = QLabel("0 caracteres")
        s.text.textChanged.connect(lambda t: lbl.setText(f"{len(t)} caracteres"))

        layout.addWidget(QLabel("Buscador con botón limpiar:"))
        layout.addWidget(s)
        layout.addWidget(lbl)
        layout.addStretch()
        return w


# ---------- MAIN ----------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())
