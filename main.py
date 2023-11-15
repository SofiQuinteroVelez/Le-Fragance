import sys
from seleccionperfumeria import Seleccionperfumeria
from PyQt5.QtGui import QFont, QPixmap, QFontDatabase
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QLabel, QApplication, QDesktopWidget


class Ventanalogin(QMainWindow):

    def __init__(self):
        super(Ventanalogin, self).__init__()

        self.setWindowTitle("Fragance Storage")
        self.setStyleSheet("color: black")
        #
        # self.ancho = 600
        # self.alto = 500
        #
        # self.resize(self.ancho, self.alto)

        # self.setFixedWidth(self.ancho)
        # self.setFixedHeight(self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Establecemos una imagen de fondo para toda la ventana
        # self.setStyleSheet("QMainWindow {background-image: url(imagenes/img.png);"
        #                    "background-repeat: no-repeat;"
        #                    "background-positions: center;}")

        # # Establecemos el fondo principal
        # self.fondo = QLabel(self)
        # # Definimos la imagen
        # self.imagenFondo = QPixmap("imagenes/img.png")
        # # Asignamos la imagen de fondo
        # self.fondo.setPixmap(self.imagenFondo)
        # # Establecer el modo para escalar la imagen
        # self.fondo.setScaledContents(True)
        # self.setCentralWidget(self.fondo)

        self.logo = QLabel(self)
        self.imagenLogo = QPixmap("imagenes/Isologotipo.png")
        self.logo.setPixmap(self.imagenLogo)
        self.logo.setScaledContents(True)
        self.logo.move(600, 270)

        self.letra1 = QFont()
        self.letra1.setFamily("Vivaldi")
        self.letra1.setPointSize(40)

        self.letra2 = QFont()
        self.letra2.setFamily("Yu Gothic UI")
        self.letra2.setPointSize(14)

        self.letrero1 = QLabel(self)
        self.letrero1.setText("Le Fragance")
        self.letrero1.setFont(self.letra1)
        self.letrero1.setStyleSheet("color: #black	;")
        self.letrero1.move(700, 250)
        self.letrero1.setFixedWidth(500)
        self.letrero1.setFixedHeight(80)

        self.letrero2 = QLabel(self)
        self.letrero2.setText("Usuario")
        self.letrero2.setFont(self.letra2)
        self.letrero2.setStyleSheet("color: black	;")
        self.letrero2.move(650, 400)
        self.letrero2.setFixedWidth(80)
        self.letrero2.setFixedHeight(50)

        self.editName = QLineEdit(self)
        self.editName.setFixedWidth(250)
        self.editName.move(650, 450)
        self.editName.setStyleSheet("background-color: ")

        self.letrero3 = QLabel(self)
        self.letrero3.setText("Contraseña")
        self.letrero3.setFont(self.letra2)
        self.letrero3.setStyleSheet("color: black	;")
        self.letrero3.move(650, 500)
        self.letrero3.setFixedWidth(120)
        self.letrero3.setFixedHeight(50)

        self.editEmail = QLineEdit(self)
        self.editEmail.setFixedWidth(250)
        self.editEmail.move(650, 550)
        self.editEmail.setStyleSheet("background-color: ")

        self.boton1 = QPushButton(self)
        self.boton1.setText('Ingresar')
        self.boton1.setStyleSheet("background-color: white ;color: black; border-radius: 10px;")
        self.boton1.setFont(self.letra2)
        self.boton1.move(700, 650)
        self.boton1.setFixedHeight(50)
        self.boton1.clicked.connect(self.metodo_ingresar)

    def metodo_ingresar(self):
        self.hide()
        self.mutante = Seleccionperfumeria()
        self.mutante.showMaximized()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    vlogin = Ventanalogin()
    vlogin.showMaximized()
    sys.exit(app.exec_())
