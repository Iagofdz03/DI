import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QMessageBox, QFileDialog,
    QColorDialog, QFontDialog, QInputDialog, QProgressDialog
)
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QColor, QFont

# Importa los UI generados por pyside6-uic
from GT1 import Ui_MainWindow      # Ventana principal
from GT2 import Ui_Dialog as Ui_NuevoProyecto
from GT3 import Ui_Dialog as Ui_ConfirmarAccion
from GT4 import Ui_Dialog as Ui_Preferencias


# --------------------------
# Diálogo: Nuevo Proyecto
# --------------------------
class DialogNuevoProyecto(QDialog, Ui_NuevoProyecto):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def get_nombre(self):
        return self.lineEdit.text().strip()


# --------------------------
# Diálogo: Confirmar acción
# --------------------------
class DialogConfirmarAccion(QDialog, Ui_ConfirmarAccion):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)


# --------------------------
# Diálogo: Preferencias de usuario
# --------------------------
class DialogPreferencias(QDialog, Ui_Preferencias):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.ruta = ""
        self.color = None       # PySide6.QtGui.QColor o None
        self.fuente = None      # PySide6.QtGui.QFont o None
        self.usuario = ""

        # Conexiones de botones
        self.pushButton.clicked.connect(self.elegir_carpeta)
        self.pushButton_2.clicked.connect(self.cambiar_color)
        self.pushButton_3.clicked.connect(self.cambiar_fuente)
        self.pushButton_4.clicked.connect(self.pedir_nombre)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def elegir_carpeta(self):
        carpeta = QFileDialog.getExistingDirectory(self, "Elegir carpeta", "")
        if carpeta:
            self.ruta = carpeta
            self.actualizar_preview()

    def cambiar_color(self):
        color = QColorDialog.getColor(parent=self)
        if color.isValid():
            self.color = color
            self.actualizar_preview()

    def cambiar_fuente(self):
        # Normalizar el resultado de QFontDialog.getFont que puede variar según versión
        result = QFontDialog.getFont(parent=self)
        fuente = None
        ok = False

        if isinstance(result, tuple) and len(result) >= 2:
            a, b = result[0], result[1]
            # caso esperado: (QFont, bool)
            if isinstance(a, QFont) and isinstance(b, bool):
                fuente, ok = a, b
            # posible caso invertido: (bool, QFont)
            elif isinstance(b, QFont) and isinstance(a, bool):
                fuente, ok = b, a
            else:
                # detectar QFont en la tupla por seguridad
                if isinstance(a, QFont):
                    fuente, ok = a, bool(b)
                elif isinstance(b, QFont):
                    fuente, ok = b, bool(a)
        elif isinstance(result, QFont):
            fuente, ok = result, True
        else:
            fuente, ok = None, False

        if ok and isinstance(fuente, QFont):
            self.fuente = fuente
            self.actualizar_preview()

    def pedir_nombre(self):
        nombre, ok = QInputDialog.getText(self, "Nombre de usuario", "Introduce tu nombre:")
        if ok and nombre.strip():
            self.usuario = nombre.strip()
            self.actualizar_preview()

    def actualizar_preview(self):
        texto = f"Usuario: {self.usuario or '—'} | Carpeta: {self.ruta or '—'}"
        self.label.setText(texto)

        if isinstance(self.color, QColor):
            pal = self.label.palette()
            pal.setColor(self.label.foregroundRole(), self.color)
            self.label.setPalette(pal)

        if isinstance(self.fuente, QFont):
            self.label.setFont(self.fuente)

# --------------------------
# Ventana principal
# --------------------------
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar botones
        self.pushButton.clicked.connect(self.abrir_nuevo_proyecto)
        self.pushButton_3.clicked.connect(self.abrir_confirmar_accion)
        self.pushButton_2.clicked.connect(self.abrir_centro_mensajes)
        self.pushButton_4.clicked.connect(self.abrir_preferencias)
        self.pushButton_5.clicked.connect(self.abrir_exportar)

    # --- Nuevo proyecto ---
    def abrir_nuevo_proyecto(self):
        dlg = DialogNuevoProyecto(self)
        if dlg.exec() == QDialog.Accepted:
            nombre = dlg.get_nombre()
            QMessageBox.information(self, "Proyecto creado", f"Proyecto '{nombre or '(sin nombre)'}' creado correctamente.")
            self.statusbar.showMessage(f"Proyecto '{nombre}' creado correctamente.", 3000)
        else:
            self.statusbar.showMessage("Creación cancelada.", 3000)

    # --- Confirmar acción ---
    def abrir_confirmar_accion(self):
        dlg = DialogConfirmarAccion(self)
        if dlg.exec() == QDialog.Accepted:
            QMessageBox.information(self, "Confirmado", "Los datos temporales se han eliminado correctamente.")
            self.statusbar.showMessage("Acción confirmada.", 3000)
        else:
            self.statusbar.showMessage("Acción cancelada.", 3000)

    # --- Centro de mensajes ---
    def abrir_centro_mensajes(self):
        QMessageBox.information(self, "Información", "Operación completada con éxito.")
        QMessageBox.warning(self, "Aviso", "Estás a punto de sobrescribir un archivo existente.")
        QMessageBox.critical(self, "Error", "Error grave en el proceso de guardado.")
        respuesta = QMessageBox.question(self, "Pregunta", "¿Deseas continuar?", QMessageBox.Yes | QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.statusbar.showMessage("El usuario decidió continuar.", 3000)
        else:
            self.statusbar.showMessage("El usuario canceló la operación.", 3000)

    # --- Preferencias de usuario ---
    def abrir_preferencias(self):
        dlg = DialogPreferencias(self)
        if dlg.exec() == QDialog.Accepted:
            resumen = f"Usuario: {dlg.usuario or '—'} | Ruta: {dlg.ruta or '—'}"
            if dlg.color:
                resumen += f" | Color: {dlg.color.name()}"
            if dlg.fuente:
                resumen += f" | Fuente: {dlg.fuente.family()}"
            QMessageBox.information(self, "Preferencias guardadas", resumen)
            self.statusbar.showMessage("Preferencias aplicadas.", 3000)
        else:
            self.statusbar.showMessage("Preferencias canceladas.", 3000)

    # --- Exportar informe ---
    def abrir_exportar(self):
        progress = QProgressDialog("Exportando informe...", "Cancelar", 0, 100, self)
        progress.setWindowModality(Qt.WindowModal)
        progress.setValue(0)

        self.valor = 0
        timer = QTimer(self)
        timer.timeout.connect(lambda: self.actualizar_progreso(progress, timer))
        timer.start(40)

        progress.exec()

    def actualizar_progreso(self, progress, timer):
        if progress.wasCanceled():
            timer.stop()
            QMessageBox.information(self, "Exportación cancelada", "El usuario canceló la exportación.")
            self.statusbar.showMessage("Exportación cancelada.", 3000)
            return

        self.valor += 2
        progress.setValue(self.valor)

        if self.valor >= 100:
            timer.stop()
            progress.setValue(100)
            QMessageBox.information(self, "Exportación completada", "El informe se ha exportado correctamente.")
            self.statusbar.showMessage("Exportación completada.", 3000)


# --------------------------
# MAIN
# --------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
