from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QListWidget
)

class PanelEmpleados(QWidget):
    def __init__(self):
        super().__init__()

        self.lista = QListWidget()
        self.inNombre = QLineEdit()
        self.inPuesto = QLineEdit()
        self.btnAdd = QPushButton("Añadir")

        form = QHBoxLayout()
        form.addWidget(QLabel("Nombre"))
        form.addWidget(self.inNombre)
        form.addWidget(QLabel("Puesto"))
        form.addWidget(self.inPuesto)
        form.addWidget(self.btnAdd)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(self.lista)

        self.btnAdd.clicked.connect(self.add_empleado)

    def add_empleado(self):
        nombre = self.inNombre.text().strip()
        puesto = self.inPuesto.text().strip()

        if nombre and puesto:
            self.lista.addItem(f"{nombre} — {puesto}")
            self.inNombre.clear()
            self.inPuesto.clear()
