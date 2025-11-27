# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGraphicsView, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 550)
        self.actionAbrirPdf = QAction(MainWindow)
        self.actionAbrirPdf.setObjectName(u"actionAbrirPdf")
        self.actionGuardarFirmado = QAction(MainWindow)
        self.actionGuardarFirmado.setObjectName(u"actionGuardarFirmado")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionAcercaDe = QAction(MainWindow)
        self.actionAcercaDe.setObjectName(u"actionAcercaDe")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widgetSeleccionPDF = QWidget(self.centralwidget)
        self.widgetSeleccionPDF.setObjectName(u"widgetSeleccionPDF")
        self.horizontalLayoutPDF = QHBoxLayout(self.widgetSeleccionPDF)
        self.horizontalLayoutPDF.setObjectName(u"horizontalLayoutPDF")
        self.horizontalLayoutPDF.setContentsMargins(0, 0, 0, 0)
        self.labelPDF = QLabel(self.widgetSeleccionPDF)
        self.labelPDF.setObjectName(u"labelPDF")

        self.horizontalLayoutPDF.addWidget(self.labelPDF)

        self.leRutaPdf = QLineEdit(self.widgetSeleccionPDF)
        self.leRutaPdf.setObjectName(u"leRutaPdf")
        self.leRutaPdf.setReadOnly(True)

        self.horizontalLayoutPDF.addWidget(self.leRutaPdf)

        self.btnExaminar = QPushButton(self.widgetSeleccionPDF)
        self.btnExaminar.setObjectName(u"btnExaminar")

        self.horizontalLayoutPDF.addWidget(self.btnExaminar)


        self.verticalLayout.addWidget(self.widgetSeleccionPDF)

        self.gvPreview = QGraphicsView(self.centralwidget)
        self.gvPreview.setObjectName(u"gvPreview")

        self.verticalLayout.addWidget(self.gvPreview)

        self.groupFirma = QGroupBox(self.centralwidget)
        self.groupFirma.setObjectName(u"groupFirma")
        self.formLayoutFirma = QFormLayout(self.groupFirma)
        self.formLayoutFirma.setObjectName(u"formLayoutFirma")
        self.labelFirmante = QLabel(self.groupFirma)
        self.labelFirmante.setObjectName(u"labelFirmante")

        self.formLayoutFirma.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelFirmante)

        self.leFirmante = QLineEdit(self.groupFirma)
        self.leFirmante.setObjectName(u"leFirmante")

        self.formLayoutFirma.setWidget(0, QFormLayout.ItemRole.FieldRole, self.leFirmante)

        self.labelMotivo = QLabel(self.groupFirma)
        self.labelMotivo.setObjectName(u"labelMotivo")

        self.formLayoutFirma.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelMotivo)

        self.leMotivo = QLineEdit(self.groupFirma)
        self.leMotivo.setObjectName(u"leMotivo")

        self.formLayoutFirma.setWidget(1, QFormLayout.ItemRole.FieldRole, self.leMotivo)

        self.btnFirmar = QPushButton(self.groupFirma)
        self.btnFirmar.setObjectName(u"btnFirmar")

        self.formLayoutFirma.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.btnFirmar)


        self.verticalLayout.addWidget(self.groupFirma)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionAbrirPdf)
        self.menuArchivo.addAction(self.actionGuardarFirmado)
        self.menuArchivo.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAcercaDe)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Firma Digital de Documentos", None))
        self.actionAbrirPdf.setText(QCoreApplication.translate("MainWindow", u"Abrir PDF", None))
        self.actionGuardarFirmado.setText(QCoreApplication.translate("MainWindow", u"Guardar PDF firmado", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionAcercaDe.setText(QCoreApplication.translate("MainWindow", u"Acerca de...", None))
        self.labelPDF.setText(QCoreApplication.translate("MainWindow", u"Archivo PDF:", None))
        self.btnExaminar.setText(QCoreApplication.translate("MainWindow", u"Examinar...", None))
        self.groupFirma.setTitle(QCoreApplication.translate("MainWindow", u"Datos de firma", None))
        self.labelFirmante.setText(QCoreApplication.translate("MainWindow", u"Nombre del firmante:", None))
        self.labelMotivo.setText(QCoreApplication.translate("MainWindow", u"Motivo de la firma:", None))
        self.btnFirmar.setText(QCoreApplication.translate("MainWindow", u"Aplicar firma al PDF", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

