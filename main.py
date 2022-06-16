from PyQt5 import uic, QtWidgets

def initial():
    tela2.show()
    tela1.close()

def second():
    tela3.show()
    tela2.close()

def third():
    tela4.show()
    tela2.close()

def back():
    tela2.show()
    tela3.close()
    tela4.close()

def out():
    tela1.close()
    tela2.close()
    tela3.close()
    tela4.close()

def confirmation():
    tela3.label_5.show()
#Configuração de telas
app = QtWidgets.QApplication([])
tela1 = uic.loadUi("Page1.ui")
tela2 = uic.loadUi("Page3.ui")
tela3 = uic.loadUi("Page2.ui")
tela4 = uic.loadUi("Page4.ui")

#Tornar funcional a página 1
tela1.pushButton.clicked.connect(initial)
tela1.pushButton_2.clicked.connect(initial)
#Tornar funcional a página 2
tela2.pushButton.clicked.connect(second)
tela2.pushButton_2.clicked.connect(third)
#Botões de saída
tela1.pushButton_3.clicked.connect(out)
tela3.pushButton_3.clicked.connect(out)
tela2.pushButton_3.clicked.connect(out)
tela4.pushButton_3.clicked.connect(out)
#Mostrar confirmação de consulta salva
tela3.label_5.close()
tela3.pushButton.clicked.connect(confirmation)
#voltar á página 2
tela3.pushButton_4.clicked.connect(back)
tela4.pushButton_4.clicked.connect(back)


tela1.show()
app.exec()
