# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Page2.ui'
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
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(530, 280, 201, 41))
        font = QFont()
        font.setFamily(u"Tw Cen MT")
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(231, 231, 231);")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(-10, -30, 871, 181))
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(108, 108, 108, 99));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.499636, stop:1 rgba(247, 247, 246, 0));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.499636, stop:1 rgba(246, 246, 247, 159));")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 50, 291, 51))
        font1 = QFont()
        font1.setFamily(u"Tw Cen MT Condensed")
        font1.setPointSize(26)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.499636, stop:1 rgba(246, 246, 247, 159));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(108, 108, 108, 0));")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 100, 291, 51))
        font2 = QFont()
        font2.setFamily(u"Tw Cen MT Condensed")
        font2.setPointSize(12)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.499636, stop:1 rgba(246, 246, 247, 159));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(108, 108, 108, 0));")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 130, 511, 41))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.499636, stop:1 rgba(246, 246, 247, 159));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(108, 108, 108, 0));")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 280, 251, 41))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"background-color: rgb(231, 231, 231);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 430, 141, 28))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(68, 134, 203);")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(380, 500, 93, 28))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(69, 137, 206);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 350, 161, 51))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.499636, stop:1 rgba(246, 246, 247, 159));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(108, 108, 108, 0));")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(710, 150, 93, 28))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(69, 137, 206);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_4.raise_()
        self.dateEdit.raise_()
        self.frame_4.raise_()
        self.comboBox.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.label_5.raise_()
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Escolha o M\u00e9dico e a especialidade desejada. ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Selecione a data e voc\u00ea receber\u00e1 a confirma\u00e7\u00e3o do seu agendamento pelo email.", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"M\u00e9dicos", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Pediatra: Manoel Lisboa", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Dentista: Manoela Soares", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Dermatologista: Daniel Garcia", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Ortopedista: Juliana Almeida", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Psic\u00f3loga: Nelma Pimentel", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Nutrcionista: Bruno Gouveia", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Salvar Consulta", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Consulta salva com sucesso!", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
    # retranslateUi

