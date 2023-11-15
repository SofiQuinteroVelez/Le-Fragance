from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton
from perfumeria1 import Perfumeria1
from perfumeria2 import  Perfumeria2
class Seleccionperfumeria(QMainWindow):

    def __init__(self):
        super(Seleccionperfumeria, self).__init__()

        self.setWindowTitle("Seleccionar la perfumeria")
        self.setStyleSheet("background-color: #FF6EB4")

        # self.ancho = 600
        # self.alto = 400
        #
        # self.resize(self.ancho, self.alto)

        # self.setFixedWidth(self.ancho)
        # self.setFixedHeight(self.alto)

        self.letra1 = QFont()
        self.letra1.setFamily("pristina")
        self.letra1.setPointSize(20)

        self.boton1 = QPushButton(self)
        self.boton1.setText('Perfumeria 1')
        self.boton1.setFont(self.letra1)
        self.boton1.move(800,300)
        self.boton1.setStyleSheet("background-color: black ;color: white; border-radius: 10px;")
        self.boton1.setFixedHeight(50)
        self.boton1.setFixedWidth(250)
        self.boton1.clicked.connect(self.metodo_perfumeria1)

        self.boton2 = QPushButton(self)
        self.boton2.setText('Perfumeria 2')
        self.boton2.setFont(self.letra1)
        self.boton2.move(800,600)
        self.boton2.setStyleSheet("background-color: black ;color: white; border-radius: 10px;")
        self.boton2.setFixedHeight(50)
        self.boton2.setFixedWidth(250)
        self.boton2.clicked.connect(self.metodo_perfumeria2)

    def metodo_perfumeria1(self):
        self.hide()
        self.p1 = Perfumeria1(self)
        self.p1.showMaximized()

    def metodo_perfumeria2(self):
        self.hide()
        self.p2 = Perfumeria2(self)
        self.p2.showMaximized()