# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Page3.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"background-color: rgb(85, 170, 255);\n"
"border-radius: 5;\n"
"border-style: solid;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, -30, 801, 181))
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(108, 108, 108, 99));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.499636, stop:1 rgba(247, 247, 246, 0));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.499636, stop:1 rgba(246, 246, 247, 159));")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 50, 291, 51))
        font = QFont()
        font.setFamily(u"Tw Cen MT Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.499636, stop:1 rgba(246, 246, 247, 159));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(108, 108, 108, 0));")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 110, 281, 31))
        font1 = QFont()
        font1.setFamily(u"Tw Cen MT Condensed")
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setMouseTracking(True)
        self.label_2.setTabletTracking(False)
        self.label_2.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(108, 108, 108, 0));")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 180, 371, 31))
        font2 = QFont()
        font2.setFamily(u"Tw Cen MT Condensed")
        font2.setPointSize(20)
        self.label_3.setFont(font2)
        self.label_3.setMouseTracking(True)
        self.label_3.setTabletTracking(False)
        self.label_3.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(108, 108, 108, 0));")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 297, 201, 71))
        font3 = QFont()
        font3.setFamily(u"Tw Cen MT")
        font3.setPointSize(12)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"background-color: rgb(68, 134, 203);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(430, 297, 201, 71))
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(68, 134, 203);")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(350, 510, 93, 28))
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(69, 137, 206);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Agendamento virtual", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Seja bem vindo ao nosso agendamento virtual!", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Selecione a a\u00e7\u00e3o que deseja realizar:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Agendar Consulta", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Visulizar Consultas", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
    # retranslateUi

