# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Page4.ui'
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
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, -30, 801, 181))
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(108, 108, 108, 99));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.499636, stop:1 rgba(247, 247, 246, 0));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.499636, stop:1 rgba(246, 246, 247, 159));")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 50, 291, 51))
        font = QFont()
        font.setFamily(u"Tw Cen MT Condensed")
        font.setPointSize(26)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.499636, stop:1 rgba(246, 246, 247, 159));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(108, 108, 108, 0));")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 100, 281, 31))
        font1 = QFont()
        font1.setFamily(u"Tw Cen MT Condensed")
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setMouseTracking(True)
        self.label_2.setTabletTracking(False)
        self.label_2.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(108, 108, 108, 0));")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(380, 500, 93, 28))
        font2 = QFont()
        font2.setFamily(u"Tw Cen MT")
        font2.setPointSize(12)
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(69, 137, 206);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 180, 521, 41))
        font3 = QFont()
        font3.setFamily(u"Tw Cen MT Condensed")
        font3.setPointSize(20)
        self.label_3.setFont(font3)
        self.label_3.setMouseTracking(True)
        self.label_3.setTabletTracking(False)
        self.label_3.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(108, 108, 108, 0));")
        self.listWidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(200, 240, 391, 101))
        font4 = QFont()
        font4.setFamily(u"Tw Cen MT")
        font4.setPointSize(10)
        self.listWidget.setFont(font4)
        self.listWidget.setStyleSheet(u"background-color: rgb(231, 231, 231);")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(710, 150, 93, 28))
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(69, 137, 206);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_4.raise_()
        self.frame_4.raise_()
        self.pushButton_3.raise_()
        self.label_3.raise_()
        self.listWidget.raise_()
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
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Agendamento virtual", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Seja bem vindo ao nosso agendamento virtual!", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Aqui voc\u00ea pode visualizar as consultas agendadas", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u" \u00b0 Psic\u00f3loga: Nelma Pimentel  22/06/2022", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u" \u00b0 Pediatra: Manoel Lisboa  25/07/2022", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u" \u00b0 Dermatologista: Daniel Garcia 31/07/2022", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
    # retranslateUi

