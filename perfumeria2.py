from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit


class Perfumeria2(QMainWindow):

    def __init__(self, ant):
        super(Perfumeria2, self).__init__()

        self.anterior = ant

        self.setWindowTitle("Inventario Perfumeria 2")
        self.setStyleSheet("background-color: #FF6EB4")

        # self.ancho = 600
        # self.alto = 400
        #
        # self.resize(self.ancho, self.alto)

        # self.setFixedWidth(self.ancho)
        # self.setFixedHeight(self.alto)

        self.letra1 = QFont()
        self.letra1.setFamily("Vivaldi")
        self.letra1.setPointSize(60)

        self.letra2 = QFont()
        self.letra2.setFamily("pristina")
        self.letra2.setPointSize(30)

        self.letrero1 = QLabel(self)
        self.letrero1.setText("Inventario")
        self.letrero1.setFont(self.letra1)
        self.letrero1.setStyleSheet("color: black	;")
        self.letrero1.move(700, 200)
        self.letrero1.setFixedWidth(400)
        self.letrero1.setFixedHeight(80)

        self.letrero2 = QLabel(self)
        self.letrero2.setText("Amber Gold")
        self.letrero2.setFont(self.letra2)
        self.letrero2.setStyleSheet("color: white	;")
        self.letrero2.move(500, 400)
        self.letrero2.setFixedWidth(400)
        self.letrero2.setFixedHeight(60)

        self.editL2 = QLineEdit(self)
        self.editL2.setFixedWidth(200)
        self.editL2.move(850, 410)
        self.editL2.setStyleSheet("background-color: ")

        self.botonMas = QPushButton(self)
        self.botonMas.setText("+")
        self.botonMas.setStyleSheet("background-color: black ;color: white; border-radius: 10px;")
        self.botonMas.move(1090, 415)
        self.botonMas.setFixedHeight(20)
        self.botonMas.setFixedWidth(20)

        self.botonMenos = QPushButton(self)
        self.botonMenos.setText("-")
        self.botonMenos.setStyleSheet("background-color: black ;color: white; border-radius: 10px;")
        self.botonMenos.move(1130, 415)
        self.botonMenos.setFixedHeight(20)
        self.botonMenos.setFixedWidth(20)

        self.letrero3 = QLabel(self)
        self.letrero3.setText("Sauvage")
        self.letrero3.setFont(self.letra2)
        self.letrero3.setStyleSheet("color: white	;")
        self.letrero3.move(500, 500)
        self.letrero3.setFixedWidth(200)
        self.letrero3.setFixedHeight(60)

        self.editL3 = QLineEdit(self)
        self.editL3.setFixedWidth(200)
        self.editL3.move(850, 510)
        self.editL3.setStyleSheet("background-color: ")

        self.botonMas1 = QPushButton(self)
        self.botonMas1.setText("+")
        self.botonMas1.setStyleSheet("background-color: black ;color: white; border-radius: 10px;")
        self.botonMas1.move(1090, 515)
        self.botonMas1.setFixedHeight(20)
        self.botonMas1.setFixedWidth(20)

        self.botonMenos1 = QPushButton(self)
        self.botonMenos1.setText("-")
        self.botonMenos1.setStyleSheet("background-color: black ;color: white; border-radius: 10px;")
        self.botonMenos1.move(1130, 515)
        self.botonMenos1.setFixedHeight(20)
        self.botonMenos1.setFixedWidth(20)

        self.boton1 = QPushButton(self)
        self.boton1.setText('Regresar')
        self.boton1.setFont(self.letra2)
        self.boton1.move(500, 800)
        self.boton1.setStyleSheet("background-color: black ;color: white; border-radius: 10px;")
        self.boton1.setFixedHeight(50)
        self.boton1.setFixedWidth(250)

        self.boton1.clicked.connect(self.metodo_regresar)

    def metodo_regresar(self):
        self.hide()
        self.anterior.showMaximized()
