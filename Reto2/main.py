import sys
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QGraphicsScene,
    QGraphicsTextItem,
)
from PySide6.QtGui import QFont
from ui_mainwindow import Ui_MainWindow

from pypdf import PdfReader, PdfWriter  # para manipular PDFs

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Ruta actual del PDF cargado
        self.ruta_pdf = None

        # Configurar interfaz
        self.statusBar().showMessage("Listo: cargue un PDF para comenzar.")

        # Conectar señales
        self.btnExaminar.clicked.connect(self.on_examinar_pdf)
        self.btnFirmar.clicked.connect(self.on_firmar_pdf)
        self.actionAbrirPdf.triggered.connect(self.on_examinar_pdf)
        self.actionGuardarFirmado.triggered.connect(self.on_guardar_firmado)
        self.actionSalir.triggered.connect(self.close)
        self.actionAcercaDe.triggered.connect(self.on_acerca_de)

        # Previsualización inicial vacía
        self._actualizar_preview("Ningún PDF cargado.")

    # ================== Previsualización ==================
    def _actualizar_preview(self, texto):
        escena = QGraphicsScene(self)
        item = QGraphicsTextItem(texto)
        fuente = QFont()
        fuente.setPointSize(12)
        item.setFont(fuente)
        escena.addItem(item)
        self.gvPreview.setScene(escena)

    # ================== Abrir PDF ==================
    def on_examinar_pdf(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar PDF",
            "",
            "Archivos PDF (*.pdf);;Todos los archivos (*)"
        )
        if not ruta:
            return
        self.ruta_pdf = ruta
        self.leRutaPdf.setText(ruta)
        nombre_archivo = ruta.split("/")[-1].split("\\")[-1]
        self._actualizar_preview(f"PDF cargado:\n{nombre_archivo}")
        self.statusBar().showMessage(f"PDF cargado: {nombre_archivo}", 3000)

    # ================== Firmar PDF ==================
    def on_firmar_pdf(self):
        if not self.ruta_pdf:
            QMessageBox.warning(self, "Aviso", "Primero debes cargar un PDF.")
            return
        firmante = self.leFirmante.text().strip()
        motivo = self.leMotivo.text().strip()
        if not firmante:
            QMessageBox.warning(self, "Aviso", "Introduce el nombre del firmante.")
            return
        if not motivo:
            QMessageBox.warning(self, "Aviso", "Introduce el motivo de la firma.")
            return
        ruta_salida, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar PDF firmado",
            "documento_firmado.pdf",
            "Archivos PDF (*.pdf);;Todos los archivos (*)"
        )
        if not ruta_salida:
            return
        try:
            self._firmar_pdf(self.ruta_pdf, ruta_salida, firmante, motivo)
        except Exception as e:
            QMessageBox.critical(self, "Error al firmar", f"Ocurrió un error:\n{e}")
            return
        self.statusBar().showMessage(f"PDF firmado guardado en: {ruta_salida}", 5000)
        QMessageBox.information(self, "Firma completada",
                                f"El PDF se ha firmado correctamente.\nRuta:\n{ruta_salida}")

    def _firmar_pdf(self, ruta_entrada, ruta_salida, firmante, motivo):
        reader = PdfReader(ruta_entrada)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        fecha_firma = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        metadata = reader.metadata or {}
        metadata.update({
            "/SignedBy": firmante,
            "/SignatureReason": motivo,
            "/SignedAt": fecha_firma
        })
        writer.add_metadata(metadata)
        with open(ruta_salida, "wb") as f:
            writer.write(f)

    # ================== Guardar desde menú ==================
    def on_guardar_firmado(self):
        QMessageBox.information(
            self,
            "Información",
            "Para guardar un PDF firmado, usa el botón 'Aplicar firma al PDF'."
        )

    # ================== Acerca de ==================
    def on_acerca_de(self):
        QMessageBox.information(
            self,
            "Acerca de DocuSecure",
            "Aplicación de Firma Digital de Documentos\n"
            "Asignatura: Desarrollo de Interfaces (2º DAM)\n"
            "Tecnologías: PySide6 + pypdf"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
